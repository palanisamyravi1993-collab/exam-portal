@echo off
set "PATH=C:\Users\ELCOT\AppData\Local\OpenAI\Codex\runtimes\cua_node\fb8898c05a62885e\bin;%PATH%"
echo ============================================================
echo Deploying ExamPortal Backend to Cloudflare Workers via CLI...
echo ============================================================
npx.cmd -y wrangler deploy
pause
