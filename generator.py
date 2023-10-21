import requests
import io
from PIL import Image
import datetime as dt
import random

now = dt.datetime.now()
filename = now.strftime("%d%m%H%M%S")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query({
    "inputs": "cloud",
    "seed": random.randint(0, 10000000),
    "steps": 100,
    "guidance_scale": 8.0,
})

image = Image.open(io.BytesIO(image_bytes))

image.save(f"./content/{filename}.jpg")
