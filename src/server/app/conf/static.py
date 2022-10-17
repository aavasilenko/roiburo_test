"""Static files settings"""

from app.conf.environ import env

STATIC_ROOT = env("STATIC_ROOT")
STATIC_URL = "/static/"
