$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot
$env:PYTHONPATH = Join-Path $PSScriptRoot "src"
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    & $python.Source -m pixel_art_skill_toolkit gui @args
} else {
    & py -3 -m pixel_art_skill_toolkit gui @args
}
