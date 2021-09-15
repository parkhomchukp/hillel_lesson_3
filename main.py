from flask import Flask, request, jsonify
import random
import string
from marshmallow import validate
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
@use_kwargs({
    "length": fields.Int(
        # required=True,
        missing=100,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def generate_password(length):
    return ''.join(
        random.choices(
            string.ascii_lowercase + string.ascii_uppercase,
            k=length
        )
    )


app.run(debug=True)
