import requests
import io
from PIL import Image
import datetime as dt
import random
from scraper import daily_word_text
# import sqlite3


now = dt.datetime.now()
filename = now.strftime("%d%m%y")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query({
    "inputs": f"{daily_word_text}",
    "seed": random.randint(0, 10000000),
    "steps": 100,
    "guidance_scale": 8.0,
})

image = Image.open(io.BytesIO(image_bytes))

image.save(f"./content/{daily_word_text}{filename}.jpg")

image_blob = io.BytesIO().getvalue()

# db = sqlite3.connect("database.db")
# c = db.cursor()
#
# c.execute("INSERT INTO images (name, data) VALUES (?, ?)",
#           (f"{daily_word_text}{filename}.jpg", image_blob))
#
# db.commit()
# db.close()

