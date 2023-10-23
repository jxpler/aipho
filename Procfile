web: gunicorn app:app
worker: celery -A celery_tasks.celery worker --loglevel=info
beat: celery -A celery_tasks.celery beat --loglevel=info
