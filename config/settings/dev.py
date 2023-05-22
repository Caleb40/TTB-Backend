import cloudinary

from .common import *

load_dotenv()

# INSTALLED_APPS.append('django_extensions')

SECRET_KEY = 'django-insecure-s#@i^qpmrb_vpfrp0o#+%1g%$7&5q2h4uy4!i*zdda%#3@bf_7'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'HOST': '127.0.0.1',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': 5432
    }
}

MIDDLEWARE.append('django_cprofile_middleware.middleware.ProfilerMiddleware', )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'TopTierBinary <noreply@toptierbinary.com>'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Custom setting. To email
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/ttb_test_media/'

CORS_ALLOW_ALL_ORIGINS = True

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

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

DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False
