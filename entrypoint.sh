#!/bin/ash

echo "Apply migrations"
python manage.py migrate

exec "$@"
