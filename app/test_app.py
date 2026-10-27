from django.test import Client

import app  # noqa: F401  (configures settings)

client = Client()


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_reads_iap_header():
    resp = client.get("/", headers={"X-Goog-Authenticated-User-Email": "accounts.google.com:a@b.co"})
    assert resp.json()["user"].endswith("a@b.co")
