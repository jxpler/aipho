import requests
import io
from PIL import Image
import random
from scraper import scrape
import os
from worker import Celery

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

celery = Celery('celery', broker=BROKER_URL)

celery.conf.timezone = 'UTC'
celery.conf.beat_schedule = {
    'update-every-midnight': {
        'task': 'generator.update',
        'schedule': '12:16',
    }
}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


@celery.task
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
