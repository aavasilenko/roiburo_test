"""Application definitions"""

INSTALLED_APPS = []

# common django apps
INSTALLED_APPS += [
    "django.contrib.auth",
    # "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
]

# Rest Framework tools
INSTALLED_APPS += [
    "rest_framework",
]

# OPENAPI docs
INSTALLED_APPS += [
    "drf_spectacular",
]

# Custom apps
INSTALLED_APPS += [
    "app",
    "core",
]
