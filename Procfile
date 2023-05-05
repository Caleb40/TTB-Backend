web: gunicorn config.wsgi
release: python manage.py migrate && python manage.py collectstatic --noinput
