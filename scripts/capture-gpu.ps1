<#
.SYNOPSIS
Capture Windows dedicated GPU memory for one known server PID.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][int]$ServerPid,
    [Parameter(Mandatory)][string]$OutputPath
)
$ErrorActionPreference = 'Stop'
$process = Get-Process -Id $ServerPid -ErrorAction Stop
$counter = Get-Counter '\GPU Process Memory(*)\Dedicated Usage' -ErrorAction Stop
$samples = @($counter.CounterSamples | Where-Object {
    $_.InstanceName -match ('^pid_' + $ServerPid + '_')
})
if (-not $samples.Count) { throw 'No dedicated GPU counter for this process; do not interpret as zero.' }
$record = [ordered]@{
    timestamp = [DateTimeOffset]::Now.ToString('o')
    pid = $ServerPid
    process_name = $process.ProcessName
    counter_instances = $samples.Count
    dedicated_gib = (($samples | Measure-Object CookedValue -Sum).Sum / 1GB)
    working_set_gib = $process.WorkingSet64 / 1GB
}
$absoluteOutput = [IO.Path]::GetFullPath($OutputPath)
[IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($absoluteOutput)) | Out-Null
[IO.File]::WriteAllText($absoluteOutput, ($record | ConvertTo-Json), [Text.UTF8Encoding]::new($false))
$record | ConvertTo-Json
