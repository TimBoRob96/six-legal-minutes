# Six Legal Minutes

Starter scaffold for your solicitor billing app.

Live app: `https://six-legal-minutes.fly.dev`

## Included
- `git` repository initialized on `main`
- Docker image setup (`Dockerfile`, `.dockerignore`)
- Fly.io config (`fly.toml`)
- Web app in `app/index.html` with legal-style calculator UI

## Local Docker run
```bash
docker build -t six-legal-minutes .
docker run --rm -p 8080:80 six-legal-minutes
```
Then open `http://localhost:8080`.

## Fly.io deploy
Prereqs:
- Fly CLI installed (`brew install flyctl`)
- Logged in (`fly auth login`)

Deploy:
```bash
# if app name is already taken, change `app` in fly.toml first
fly launch --no-deploy
fly deploy
```

## Deployment (recommended)
This repo auto-deploys to Fly.io using GitHub Actions on every push to `main`.

Workflow:
- File: `.github/workflows/deploy.yml`
- Trigger: `push` to `main` (also supports manual `workflow_dispatch`)
- Command run by CI: `flyctl deploy --remote-only --config fly.toml`

Required GitHub secret:
- `FLY_API_TOKEN` (set in repo Settings -> Secrets and variables -> Actions)

Release steps:
```bash
git add .
git commit -m "Your change summary"
git push origin main
```

Then monitor:
- GitHub Actions run for "Deploy to Fly"
- Live URL: `https://six-legal-minutes.fly.dev`
