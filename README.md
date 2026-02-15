# Six Legal Minutes

Starter scaffold for your solicitor billing app.

## Included
- `git` repository initialized on `main`
- Docker image setup (`Dockerfile`, `.dockerignore`)
- Fly.io config (`fly.toml`)
- Placeholder web page in `app/index.html`

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

## Next step
Replace `app/index.html` with your calculator UI and logic.
