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
    length = request.args.get('length', 10)

    if not length.isdigit():
        return 'ERROR: not an integer'

    length = int(length)

    if not 8 <= length <= 100:
        return 'ERROR: out of range'

    return ''.join(
        random.choices(
            string.ascii_lowercase + string.ascii_uppercase,
            k=length
        )
    )


app.run(debug=True)
