"""Smallest useful Django app: one settings block, one URL, one view."""
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import JsonResponse
from django.urls import path

settings.configure(
    DEBUG=os.getenv("DEBUG") == "1",
    SECRET_KEY=os.getenv("SECRET_KEY", "dev-only"),
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)


def whoami(request):
    # IAP puts the verified user in this header; the app never sees a password.
    email = request.headers.get("X-Goog-Authenticated-User-Email", "anonymous")
    return JsonResponse({"user": email})


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [path("", whoami), path("health", health)]

django.setup()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
