@echo off
echo Pushing ExamPortal to GitHub repository...
git push -u origin main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==============================================
    echo Success! Code pushed to:
    echo https://github.com/palanisamyravi1993-collab/exam-portal
    echo ==============================================
) else (
    echo.
    echo Push encountered an error. Please verify the repo exists at:
    echo https://github.com/new (Repository name: exam-portal)
)
