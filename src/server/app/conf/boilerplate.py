"""Boilerplate"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

WSGI_APPLICATION = "app.wsgi.application"
ROOT_URLCONF = "app.urls"
