from flask import Flask, render_template
from scraper import daily_word_text, definition_text, main_atr_text
app = Flask(__name__)


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
    app.run(debug=True, port=8080)
