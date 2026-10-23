# ExamPortal - Advanced Online Examination Platform

An enterprise-ready, high-integrity online examination platform built with **FastAPI**, **SQLAlchemy**, and a modern **Tailwind CSS Glassmorphic Single-Page Application (SPA)**.

---

## Key Features & Upscale Enhancements

- **Modern Glassmorphic UI**: Polished dark theme with Google Fonts (Plus Jakarta Sans & JetBrains Mono), responsive design, and smooth micro-animations.
- **Request Rate Limiting (100 req/hour)**: Integrated high-concurrency sliding window rate limiter enforcing a maximum of 100 requests per hour per client/IP, with standard `X-RateLimit-*` and `Retry-After` headers.
- **Full Assessment Workflow**:
  - **Student Portal**: Timed assessments, color-coded question palette, auto-save, question review marking, and anti-cheat window-blur logging.
  - **Faculty Hub**: Exam scheduler, multi-type question bank preview, candidate batch assigner, and automated grading.
  - **Subjective Manual Grading**: Interface and endpoint to review student submission sheets and assign marks for `SHORT` answer questions.
  - **Question Analytics**: Real-time accuracy percentage bars per question.
  - **Candidate Export**: Instant download of final results in Excel (`.xlsx`) or CSV.
- **Safe Exam Browser (SEB)**: Native `.seb` configuration download and request hash validation (`X-SafeExamBrowser-RequestHash = sha256(URL + seb_key)`).
- **Public & Guest Self-Registration**: Direct exam entry using a shared exam access code (e.g. `GATE2026`).

---

## Environment Variables

Configure your local or production environment in `.env` (refer to `.env.example`):

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `change-me-...` | Cryptographic secret for signing auth tokens (HMAC-SHA256). |
| `DATABASE_URL` | `sqlite:///./exam.db` | Database connection string (SQLite or PostgreSQL). |
| `PUBLIC_URL` | `http://localhost:8000` | Backend canonical URL (required for SEB request hashing). |
| `RATE_LIMIT_PER_HOUR` | `100` | Maximum allowed API requests per hour per client (HTTP 429 when exceeded). |
| `CORS_ORIGINS` | `*` | Allowed CORS origins for decoupling frontend (Vercel) from backend (Cloudflare). |
| `PORT` | `8000` | Application server port. |

---

## Local Development

```bash
# 1. Activate virtual environment
.\venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start development server
uvicorn main:app --reload --port 8000
```
Open **http://localhost:8000** in your browser.

### Default Demo Logins
- **Admin**: `admin` / `admin123`
- **Faculty**: `faculty1` / `faculty123`
- **Student**: `21AIML001` to `21AIML005` / `student123`
- **Public Exam Code**: `GATE2026`

---

## Deployment via CLI

### 1. Deploy Frontend on Vercel
The repository includes `vercel.json` configured for zero-configuration deployment:

```bash
# Using Vercel CLI:
npx vercel deploy --prod
```
When deployed on Vercel, click **Backend URL** in the bottom footer to point the frontend to your live backend endpoint.

### 2. Deploy Backend on Cloudflare (Workers / Containers)
The repository includes `wrangler.toml` preconfigured for Python Cloudflare Workers:

```bash
# Using Cloudflare Wrangler CLI:
npx wrangler deploy
```

### 3. Docker & Docker Compose
```bash
docker compose up --build
```
