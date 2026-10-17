# Install a pinned portable AutoHotkey and an explicit-launch shortcut, no startup task.
param([string]$Root='E:\llm')
$ErrorActionPreference='Stop'
$rootPath=[IO.Path]::GetFullPath($Root).TrimEnd('\')
if (-not (Test-Path -LiteralPath (Join-Path $rootPath 'runtime-config.json'))) {
    throw 'Set up the reviewed runtime and start-server.ps1 before installing the widget.'
}
$version='2.0.30'
$expected='1e0ece7ecb2d5646e55758150472677996a57f9db5c83d2996d8b47b9e2f31a4'
$url="https://github.com/AutoHotkey/AutoHotkey/releases/download/v$version/AutoHotkey_$version.zip"
$downloads=Join-Path $rootPath 'downloads'
$destination=Join-Path $rootPath "tools\AutoHotkey-$version"
$widget=Join-Path $rootPath 'widget'
New-Item -ItemType Directory -Force -Path $downloads,$widget | Out-Null
$archive=Join-Path $downloads "AutoHotkey_$version.zip"
if (-not (Test-Path -LiteralPath $archive)) { Invoke-WebRequest -UseBasicParsing $url -OutFile $archive }
if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLower() -ne $expected) {
    throw 'AutoHotkey archive hash mismatch. No executable installed.'
}
Add-Type -AssemblyName System.IO.Compression.FileSystem
if (-not (Test-Path -LiteralPath $destination)) {
    # Inspect every destination before extraction; never allow archive traversal.
    $zip=[IO.Compression.ZipFile]::OpenRead($archive)
    try {
        foreach($entry in $zip.Entries) {
            $target=[IO.Path]::GetFullPath((Join-Path $destination $entry.FullName))
            if (-not $target.StartsWith($destination+'\',[StringComparison]::OrdinalIgnoreCase) -or
                $entry.FullName -match ':|(^|[\\/])\.\.([\\/]|$)' -or
                (($entry.ExternalAttributes -shr 16) -band 0xF000) -eq 0xA000) {
                throw 'Unsafe path in AutoHotkey archive.'
            }
        }
    } finally { $zip.Dispose() }
    [IO.Compression.ZipFile]::ExtractToDirectory($archive,$destination)
}
$exe=Join-Path $destination 'AutoHotkey64.exe'
if (-not (Test-Path -LiteralPath $exe)) { throw 'Portable AutoHotkey64.exe is missing.' }
# Verify an existing installation against the verified archive, not mere presence.
$zip=[IO.Compression.ZipFile]::OpenRead($archive)
try {
    $entry=$zip.GetEntry('AutoHotkey64.exe')
    $stream=$entry.Open()
    $sha=[Security.Cryptography.SHA256]::Create()
    try { $expectedExe=([BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-','') }
    finally { $stream.Dispose(); $sha.Dispose() }
} finally { $zip.Dispose() }
if ((Get-FileHash -LiteralPath $exe).Hash -ne $expectedExe) { throw 'Installed executable differs from archive.' }
Add-Type -AssemblyName System.Drawing
Add-Type -TypeDefinition 'using System; using System.Runtime.InteropServices; public static class LabIcon { [DllImport("user32.dll")] public static extern bool DestroyIcon(IntPtr h); }'
foreach($pair in @(@('green','#86E3A7'),@('red','#FF9A9E'),@('amber','#FFD07D'))) {
    $bitmap=New-Object Drawing.Bitmap(32,32)
    $graphics=[Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode=[Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $brush=New-Object Drawing.SolidBrush([Drawing.ColorTranslator]::FromHtml($pair[1]))
    $ink=New-Object Drawing.SolidBrush([Drawing.ColorTranslator]::FromHtml('#16202D'))
    $graphics.FillEllipse($brush,2,2,28,28)
    $graphics.FillEllipse($ink,9,11,4,5)
    $graphics.FillEllipse($ink,19,11,4,5)
    $pen=New-Object Drawing.Pen($ink,2)
    $graphics.DrawArc($pen,10,15,12,8,10,160)
    $handle=$bitmap.GetHicon()
    $icon=[Drawing.Icon]::FromHandle($handle)
    $file=[IO.File]::Create((Join-Path $widget ($pair[0]+'.ico')))
    try { $icon.Save($file) } finally {
        $file.Dispose(); $icon.Dispose(); [LabIcon]::DestroyIcon($handle) | Out-Null
        $pen.Dispose(); $brush.Dispose(); $ink.Dispose(); $graphics.Dispose(); $bitmap.Dispose()
    }
}
$shell=New-Object -ComObject WScript.Shell
$shortcut=$shell.CreateShortcut((Join-Path $rootPath 'Local LLM Widget.lnk'))
$shortcut.TargetPath=$exe
$shortcut.Arguments='"'+(Join-Path $PSScriptRoot 'LocalLLM.ahk')+'" "'+$rootPath+'"'
$shortcut.WorkingDirectory=$rootPath
$shortcut.IconLocation=(Join-Path $widget 'green.ico')+',0'
$shortcut.Description='Local LLM resources and power control. Ctrl+Alt+L toggles the model.'
$shortcut.Save()
[PSCustomObject]@{Version=$version;ArchiveSHA256=$expected;ExecutableSHA256=$expectedExe.ToLower();Source=$url;Installed=(Get-Date).ToString('o')} |
    ConvertTo-Json | Set-Content -Encoding UTF8 -LiteralPath (Join-Path $widget 'installation.json')
Write-Output "Installed. Launch: $rootPath\Local LLM Widget.lnk. No Windows startup entry added."
