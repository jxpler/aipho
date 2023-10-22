from flask import Flask, render_template

app = Flask(__name__)


@app.route('/gallery/', methods=["POST", "GET"])
def home():
    return render_template('gallery.html')


@app.route('/', methods=["GET"])
def redirect():
    return home()


@app.route('/about/', methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)