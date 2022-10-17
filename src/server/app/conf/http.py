"""Http settings"""

from corsheaders.defaults import default_headers

from app.conf.environ import env

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = default_headers + ("Access-Control-Allow-Origin",)

CSRF_TRUSTED_ORIGINS = ["127.0.0.1", "localhost"]
INTERNAL_IPS = ("127.0.0.1",)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

REQUEST_LOGGING_SENSITIVE_HEADERS = [
    "Cookie",
]

BASE_URL = env("BASE_URL", default="http://127.0.0.1:8000")
