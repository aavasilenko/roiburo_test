"""Logging settings"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "common": {"format": "%(asctime)-15s %(levelname)-9s %(name)-4s %(message)-4s"},
    },
    "handlers": {
        "handler_common": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 5 * 5,
            "backupCount": 3,
            "filename": "log/common.log",
            "formatter": "common",
        },
        "handler_requests": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 5 * 5,
            "backupCount": 3,
            "filename": "log/requests.log",
            "formatter": "common",
        },
        "handler_test": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 5 * 5,
            "backupCount": 3,
            "filename": "log/test.log",
            "formatter": "common",
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "common",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": [
                "console",
            ],
        },
        "common": {
            "handlers": ["console", "handler_common"],
            "level": "DEBUG",
            "propagate": False,
        },
        "test": {
            "handlers": ["console", "handler_test"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "handler_requests"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
