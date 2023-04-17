from .common import *

SECRET_KEY = 'django-insecure-s#@i^qpmrb_vpfrp0o#+%1g%$7&5q2h4uy4!i*zdda%#3@bf_7'

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        # 'HOST': '127.0.0.1',
        'USER': os.getenv('DB_USER'),
        # 'PASSWORD': os.getenv('DB_PASSWORD'),
        # 'PORT': 5432
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Custom setting. To email
RECIPIENT_ADDRESS = os.getenv('RECIPIENT_ADDRESS')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/test_media/'
