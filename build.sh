#!/usr/bin/env bash

set -o errexit  # exit on error

pipenv install

python manage.py collectstatic --no-input
python manage.py migrate
