#!/bin/sh

if [ "$MODE" = "web" ]; then
    python manage.py migrate
    python manage.py collectstatic --no-input
    gunicorn --workers 3 --max-requests 250 --max-requests-jitter 20 abantether.wsgi:application --bind 0.0.0.0:8000


elif [ "$MODE" = "worker" ]; then
    celery -A abantether worker --loglevel=info

else
    echo "MODE env var is not set"
    exec "$@"
fi
