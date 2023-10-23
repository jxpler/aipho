import requests
import io
from PIL import Image
import datetime as dt
import random
from scraper import daily_word_text, definition_text
from config import API_URL, headers


now = dt.datetime.now()
filename = now.strftime("%d%m%y")


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query({
    "inputs": f"{daily_word_text}, {definition_text}",
    "seed": random.randint(0, 10000000),
    "steps": 250,
    "guidance_scale": 4.0,
})

image = Image.open(io.BytesIO(image_bytes))

image.save(f"./static/images/daily_word.jpg")
