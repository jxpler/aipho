from celery import Celery
import os

CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

app = Celery(
    'celery',
    broker=CELERY_BROKER_URL,
    backend=CELERY_BROKER_URL
)

app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
