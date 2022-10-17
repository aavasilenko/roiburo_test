"""Storage settings"""

from app.conf.environ import env

DEFAULT_FILE_STORAGE = env(
    "DEFAULT_FILE_STORAGE",
    cast=str,
    default="django.core.files.storage.FileSystemStorage",
)

FILE_UPLOAD_TEMP_DIR = "/tmp"
FILE_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024  # 100 Mb
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
]
DATA_UPLOAD_MAX_MEMORY_SIZE = FILE_UPLOAD_MAX_MEMORY_SIZE
