@echo off
echo ========================================
echo Pushing Object Detection Project to GitHub
echo ========================================
echo.

REM Check if git is installed
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    echo.
    echo After installing Git, run this script again.
    pause
    exit /b 1
)

echo Git is installed. Proceeding...
echo.

REM Initialize git if not already initialized
if not exist .git (
    echo Initializing git repository...
    git init
)

REM Add all files
echo Adding files...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %ERRORLEVEL% EQU 0 (
    echo No changes to commit.
) else (
    echo Creating commit...
    git commit -m "Initial commit: Object Detection ML Project"
)

REM Check if remote exists
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Adding remote repository...
    git remote add origin https://github.com/anizxx/Object-Detection.git
) else (
    echo Remote already configured.
)

REM Set main branch
git branch -M main

REM Push to GitHub
echo.
echo Pushing to GitHub...
echo You may be prompted for your GitHub credentials.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo SUCCESS! Code pushed to GitHub!
    echo ========================================
    echo Repository: https://github.com/anizxx/Object-Detection
) else (
    echo.
    echo ========================================
    echo ERROR: Push failed!
    echo ========================================
    echo.
    echo Possible issues:
    echo 1. Authentication required - use GitHub Personal Access Token
    echo 2. Repository doesn't exist or you don't have access
    echo 3. Check your internet connection
    echo.
    echo For authentication help, see: https://docs.github.com/en/authentication
)

pause


