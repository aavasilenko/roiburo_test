"""Media settings"""

import os

from app.conf.boilerplate import BASE_DIR

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
