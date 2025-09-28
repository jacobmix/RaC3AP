$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

$zipPath = Join-Path $scriptDir "rac3.zip"
$apworldPath = Join-Path $scriptDir "rac3.apworld"
$sourceFolder = Join-Path $scriptDir "rac3"

Write-Host "Preparing to zip world..."
if (Test-Path $zipPath) {
    Write-Host "Removing existing rac3.zip..."
    Remove-Item $zipPath
}
if (Test-Path $apworldPath) {
    Write-Host "Removing existing rac3.apworld..."
    Remove-Item $apworldPath
}

Write-Host "Zipping world folder to rac3.zip..."
Compress-Archive -Path $sourceFolder -DestinationPath $zipPath -Force

Write-Host "Renaming rac3.zip to rac3.apworld..."
Rename-Item -Path $zipPath -NewName "rac3.apworld"

Write-Host "Done! Output: $apworldPath"