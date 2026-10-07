[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$codexRoot = Join-Path $env:USERPROFILE '.codex'
$skillsRoot = Join-Path $codexRoot 'skills'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'

New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null

foreach ($skill in Get-ChildItem -LiteralPath (Join-Path $repoRoot 'skills') -Directory) {
    $destination = Join-Path $skillsRoot $skill.Name
    if (Test-Path -LiteralPath $destination) {
        Move-Item -LiteralPath $destination -Destination "$destination.backup-$stamp"
    }
    Copy-Item -LiteralPath $skill.FullName -Destination $destination -Recurse
    Write-Host "Installed skill: $($skill.Name)"
}

$agentsSource = Join-Path $repoRoot 'AGENTS.md'
$agentsDestination = Join-Path $codexRoot 'AGENTS.md'
if (Test-Path -LiteralPath $agentsDestination) {
    Copy-Item -LiteralPath $agentsDestination -Destination "$agentsDestination.backup-$stamp"
}
Copy-Item -LiteralPath $agentsSource -Destination $agentsDestination

Write-Host 'Installed global AGENTS.md.'
Write-Host 'Restart Codex to load the installed skills and instructions.'
