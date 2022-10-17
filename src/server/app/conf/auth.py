from app.conf.environ import env

SECRET_KEY = env("SECRET_KEY")

# AUTH_USER_MODEL = "account.AppUser"

# AUTHENTICATION_BACKENDS = (
#    "django.contrib.auth.backends.ModelBackend",
#    "core.backends.PhoneBackend",
# )
