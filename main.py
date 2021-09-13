from flask import Flask
from flask import request
import random
import string

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def generate_password():
    length = request.args['length']
    return ''.join(random.choices(
        string.ascii_lowercase + string.ascii_uppercase,
        k=int(length)
    ))


app.run(debug=True)