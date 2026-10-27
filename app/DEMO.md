# Demo: Django behind IAP

**Framework:** Django (Python), written as a single file. **Moving parts locally:** none. No database or migrations are configured.

`/` echoes the user that Identity-Aware Proxy verified, so you can see zero-trust access working in the cloud. Locally there is no IAP, so you fake the header.

## Run it

```bash
cd app
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

```bash
pytest                              # 2 tests
python app.py runserver 8000        # http://localhost:8000
```

## Try it

```bash
curl localhost:8000/                # {"user":"anonymous"}
curl -H 'X-Goog-Authenticated-User-Email: accounts.google.com:you@example.com' localhost:8000/
curl localhost:8000/health
```

## Docker

```bash
docker build -t iap-demo . && docker run -p 8000:8000 iap-demo
```

## What to learn

A normal Django project spreads this over `manage.py`, `settings.py`, `urls.py` and `views.py`. Here `settings.configure()`, `urlpatterns` and the views sit together so the whole shape is visible. When you want the conventional layout, run `django-admin startproject demo` and compare.

In production the header can be spoofed unless traffic only arrives through IAP. Verify the signed JWT (`X-Goog-IAP-JWT-Assertion`) before you trust it.
