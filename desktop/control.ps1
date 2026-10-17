# Operate only the existing configured local model; never kill by image name.
param(
    [Parameter(Mandatory=$true)][string]$Root,
    [ValidateSet('Toggle','Start','Stop')][string]$Action='Toggle',
    [string]$ResultFile
)
$ErrorActionPreference='Stop'
$rootPath=[IO.Path]::GetFullPath($Root).TrimEnd('\')
$widgetDir=Join-Path $rootPath 'widget'
if (-not $ResultFile) { $ResultFile=Join-Path $widgetDir 'action.ini' }
$resultPath=[IO.Path]::GetFullPath($ResultFile)
if (-not $resultPath.StartsWith($widgetDir+'\',[StringComparison]::OrdinalIgnoreCase)) {
    throw 'Result file must be inside the widget directory.'
}
$mutex=New-Object Threading.Mutex($false,'Local\LocalCodingLabControl')
$locked=$false
$status='error'
$message='Control failed.'
try {
    $locked=$mutex.WaitOne(0)
    if (-not $locked) { throw 'Another model action is already in progress.' }
    $config=Get-Content -LiteralPath (Join-Path $rootPath 'runtime-config.json') -Raw | ConvertFrom-Json
    $statePath=Join-Path $rootPath 'server-settings.json'
    $idleDescription='30 minutes'
    if (Test-Path -LiteralPath $statePath) {
        $prior=Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
        if ($prior.idle_seconds -and $prior.idle_seconds -ne 1800) {
            $idleDescription="$($prior.idle_seconds) seconds (test setting)"
        }
    }
    $all=@(Get-CimInstance Win32_Process -Filter "Name='llama-server.exe'")
    $owned=@($all | Where-Object {
        $_.ExecutablePath -eq $config.runtime_executable -and
        $_.CommandLine.Contains([string]$config.model) -and
        $_.CommandLine -match '(?:^|\s)--port(?:\s+|=)8080(?:\s|$)'
    })
    if ($all.Count -ne $owned.Count -or $owned.Count -gt 1) {
        throw 'An unrelated or ambiguous inference server exists. Nothing changed.'
    }
    $sleeping=$false
    if ($owned.Count) {
        $props=Invoke-RestMethod 'http://127.0.0.1:8080/props' -TimeoutSec 5
        if ($props.model_alias -ne $config.alias) { throw 'Endpoint model identity differs.' }
        $sleeping=[bool]$props.is_sleeping
    }
    if ($Action -eq 'Toggle') {
        $Action=if ($owned.Count -and -not $sleeping) {'Stop'}else{'Start'}
    }
    if ($Action -eq 'Stop' -and $owned.Count) {
        $state=Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
        $run=[IO.Path]::GetFullPath([string]$state.run_directory)
        $stop=[IO.Path]::GetFullPath([string]$state.stop_file)
        if ($state.pid -ne $owned[0].ProcessId -or $state.model -ne $config.model -or
            -not $run.StartsWith($rootPath+'\logs\',[StringComparison]::OrdinalIgnoreCase) -or
            -not $stop.StartsWith($rootPath+'\logs\',[StringComparison]::OrdinalIgnoreCase)) {
            throw 'Saved ownership receipt does not match the live server.'
        }
        $process=Get-Process -Id $owned[0].ProcessId
        $receipt=Get-Content -LiteralPath (Join-Path $run 'process.json') -Raw | ConvertFrom-Json
        $manager=Get-CimInstance Win32_Process -Filter "ProcessId=$($receipt.launcher_pid)"
        # A Windows venv launcher starts a second Python process. Verify the live
        # ancestry and exact session paths instead of assuming these PIDs match.
        if ($receipt.pid -ne $process.Id -or $owned[0].ParentProcessId -ne $receipt.launcher_pid -or
            -not $manager -or
            ($manager.ProcessId -ne $state.manager_pid -and $manager.ParentProcessId -ne $state.manager_pid) -or
            -not $manager.CommandLine.Contains((Join-Path $rootPath 'local-coding-lab\lab.py')) -or
            -not $manager.CommandLine.Contains($stop) -or $receipt.stop_file -ne $stop -or
            $process.Path -ne $config.runtime_executable -or
            [math]::Abs(($process.StartTime.ToUniversalTime()-$owned[0].CreationDate.ToUniversalTime()).Ticks) -ge 10) {
            throw 'Process identity changed; stop refused.'
        }
        New-Item -ItemType File -Force -Path $stop | Out-Null
        if (-not $process.WaitForExit(20000)) { throw 'Stop requested; model has not exited yet.' }
        $status='stopped'
        $message='Model stopped. Its memory is released. Toggle again before chatting.'
    } elseif ($Action -eq 'Stop') {
        $status='stopped'; $message='Model is already stopped.'
    } elseif ($sleeping) {
        # Tokenization wakes the runtime without generating or modifying editor chat.
        Invoke-RestMethod 'http://127.0.0.1:8080/tokenize' -Method Post -ContentType 'application/json' -Body '{"content":""}' -TimeoutSec 600 | Out-Null
        $status='ready'; $message="Model awake. It will sleep after $idleDescription idle."
    } elseif ($owned.Count) {
        $status='ready'; $message='Model is already loaded.'
    } else {
        & (Join-Path $rootPath 'start-server.ps1')
        $status='ready'; $message='Model loaded. It will sleep after 30 minutes idle.'
    }
} catch {
    $message=$_.Exception.Message -replace '[\r\n]+',' '
} finally {
    if ($locked) { $mutex.ReleaseMutex() }
    $mutex.Dispose()
    $safeMessage=$message -replace '[\r\n]+',' '
    "[result]`r`nstatus=$status`r`nmessage=$safeMessage`r`ntime=$((Get-Date).ToString('o'))" |
        Set-Content -LiteralPath ($resultPath+'.tmp') -Encoding Unicode
    Move-Item -LiteralPath ($resultPath+'.tmp') -Destination $resultPath -Force
}
if ($status -eq 'error') { exit 1 }
