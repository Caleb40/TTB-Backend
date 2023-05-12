release:
    python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi
web:
    gunicorn config.wsgi