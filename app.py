from flask import Flask, render_template
from scraper import daily_word_text, definition_text, main_atr_text
from celery import Celery
import os
from generator import update

app = Flask(__name__)

celery = Celery(app.import_name, broker=os.environ.get("REDIS_URL"))
celery.conf.update(app.config)
celery.config_from_object('celeryconfig')


@app.route('/home/', methods=["POST", "GET"])
def home():
    word = daily_word_text.capitalize()
    return render_template('home.html', word=word, definition=definition_text, atr=main_atr_text)


@app.route('/', methods=["GET"])
def redirect():
    return home()


@app.route('/about/', methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
