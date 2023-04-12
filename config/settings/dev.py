from .common import *

SECRET_KEY = 'django-insecure-s#@i^qpmrb_vpfrp0o#+%1g%$7&5q2h4uy4!i*zdda%#3@bf_7'

DEBUG = True

ALLOWED_HOSTS = []

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
