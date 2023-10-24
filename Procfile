web: gunicorn app:app
worker: celery -A worker.celery worker --loglevel=info
beat: celery -A worker.celery beat --loglevel=info