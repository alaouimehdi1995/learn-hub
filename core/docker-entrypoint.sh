#!/bin/sh

# This script will be executed at each `docker-compose up` command,
# to make sure the django migrations are installed.

echo "> Applying database migrations"
python manage.py migrate

echo "> Starting server"
python manage.py runserver 0.0.0.0:8000
