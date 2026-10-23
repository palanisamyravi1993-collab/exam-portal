@echo off
set "PATH=C:\Users\ELCOT\AppData\Local\OpenAI\Codex\runtimes\cua_node\fb8898c05a62885e\bin;%PATH%"
echo ============================================================
echo Deploying ExamPortal Frontend to Vercel via CLI...
echo ============================================================
npx.cmd -y vercel deploy --prod
pause
