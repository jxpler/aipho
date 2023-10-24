import requests
import io
from PIL import Image
import random
from scraper import scrape
import os
from worker import Celery

API_URL = os.environ["API_URL"]
headers = {"Authorization": os.environ["AUTH_TOKEN"]}
BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

app = Celery('app', broker=BROKER_URL)

app.conf.timezone = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'update-every-midnight': {

        'task': 'generator.update',
        'schedule': '0 4 * * *',
    },
}


@app.task
def update():
    daily_word_text, main_atr_text, definition_text = scrape()

    img_path = "./static/images/daily_word.jpg"

    if os.path.exists(img_path):
        os.remove(img_path)

    image_bytes = query({
        "inputs": f"{daily_word_text}, {definition_text}",
        "seed": random.randint(0, 10000000),
        "steps": 250,
        "guidance_scale": 4.0,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save(img_path)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
