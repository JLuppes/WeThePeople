from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/poll', methods=["GET", "POST"])
def pollPage():

    if request.method == "POST":

        name = request.form.get('name')

        return render_template('pollSuccess.html', name=name)

    return render_template('poll.html')
