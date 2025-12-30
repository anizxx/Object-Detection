# PowerShell script to push to GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Pushing Object Detection Project to GitHub" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $null = Get-Command git -ErrorAction Stop
    Write-Host "Git is installed. Proceeding..." -ForegroundColor Green
} catch {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installing Git, run this script again." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Initialize git if not already initialized
if (-not (Test-Path .git)) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
}

# Add all files
Write-Host "Adding files..." -ForegroundColor Yellow
git add .

# Check if there are changes to commit
$status = git status --porcelain
if ($status) {
    Write-Host "Creating commit..." -ForegroundColor Yellow
    git commit -m "Initial commit: Object Detection ML Project"
} else {
    Write-Host "No changes to commit." -ForegroundColor Yellow
}

# Check if remote exists
try {
    $null = git remote get-url origin 2>$null
    Write-Host "Remote already configured." -ForegroundColor Green
} catch {
    Write-Host "Adding remote repository..." -ForegroundColor Yellow
    git remote add origin https://github.com/anizxx/Object-Detection.git
}

# Set main branch
git branch -M main

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "You may be prompted for your GitHub credentials." -ForegroundColor Yellow
Write-Host ""

$pushResult = git push -u origin main 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "SUCCESS! Code pushed to GitHub!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Repository: https://github.com/anizxx/Object-Detection" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "ERROR: Push failed!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible issues:" -ForegroundColor Yellow
    Write-Host "1. Authentication required - use GitHub Personal Access Token" -ForegroundColor Yellow
    Write-Host "2. Repository doesn't exist or you don't have access" -ForegroundColor Yellow
    Write-Host "3. Check your internet connection" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For authentication help, see: https://docs.github.com/en/authentication" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Error details:" -ForegroundColor Red
    Write-Host $pushResult -ForegroundColor Red
}

Read-Host "Press Enter to exit"





