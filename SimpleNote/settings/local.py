from .base import *

DEBUG = True

ALLOWED_HOSTS = ["37.32.14.9"]

# Local SQLite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}