<#!
.SYNOPSIS
Show or apply a pinned Windows CUDA setup. Requires Python 3.11+ on PATH.
.EXAMPLE
.\scripts\setup.ps1 -Python E:\llm\python\Scripts\python.exe -Model gemma4-26b-qat
.EXAMPLE
.\scripts\setup.ps1 -Model gemma4-26b-qat -Apply
#>
[CmdletBinding()]
param(
    [string]$Python = 'python',
    [string]$DataDir = (Join-Path (Split-Path $PSScriptRoot -Parent) 'local-data'),
    [ValidateSet('qwen36-q4', 'gemma4-26b-qat', 'glm47-udq4', 'glm47-q5')]
    [string]$Model = 'gemma4-26b-qat',
    [switch]$Apply,
    [switch]$SkipRuntime
)
$ErrorActionPreference = 'Stop'
$lab = Join-Path (Split-Path $PSScriptRoot -Parent) 'lab.py'
& $Python -c 'import sys; assert sys.version_info >= (3, 11), "Python 3.11+ required"'
if ($LASTEXITCODE -ne 0) { throw 'Install Python 3.11+ or pass -Python with its path.' }
& $Python $lab --data-dir $DataDir doctor
if ($LASTEXITCODE -ne 0) { throw 'Doctor failed.' }
$applyArgs = @()
if ($Apply) { $applyArgs = @('--apply') }
if (-not $SkipRuntime) {
    & $Python $lab --data-dir $DataDir install-runtime @applyArgs
    if ($LASTEXITCODE -ne 0) { throw 'Runtime setup stopped; see message above.' }
}
& $Python $lab --data-dir $DataDir download-model $Model @applyArgs
if ($LASTEXITCODE -ne 0) { throw 'Model download stopped; see message above.' }
Write-Host 'Setup finished. No model was started. See docs/setup.md for launch and benchmark steps.'
