import dj_database_url

from .common import *

DEBUG = os.environ['DEBUG']

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['ttbserver.up.railway.app', 'ttb-backend.onrender.com']

DATABASES = {
    'default': dj_database_url.config()
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_SECRET'),
}

# For testing cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/ttb_media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'TopTierBinary <noreply@toptierbinary.com>'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file", "console"]},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": os.environ.get('FILE_LOG_LEVEL', 'DEBUG'),
            "class": "logging.FileHandler",
            "filename": "django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        'django': {
            "handlers": ['console', 'file'],
            "level": os.environ.get('DJANGO_LOG_LEVEL', 'DEBUG'),
            "propagate": True

        }
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
