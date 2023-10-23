from celery import Celery
import os

broker_url = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

app = Celery(
    'celery',
    broker=broker_url,
    backend=broker_url
)

app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
