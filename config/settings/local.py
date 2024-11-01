from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

THIRD_PARTY_APPS = []

INSTALLED_APPS += THIRD_PARTY_APPS