import random
import string
import requests
from flask import Flask, request, jsonify, Response
from webargs.flaskparser import use_kwargs
from data_validation import password_args, bitcoin_rate_args

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


@app.route("/password")
@use_kwargs(password_args, location="query")
def generate_password(length, specials, digits):
    characters = string.ascii_lowercase + string.ascii_uppercase
    if specials == 1:
        characters += '''!"№;%:?*$()_+'''
    if digits == 1:
        characters += string.digits
    return ''.join(
        random.choices(
            characters,
            k=length
        )
    )


@app.route('/bitcoin_rate')
@use_kwargs(bitcoin_rate_args, location="query")
def get_bitcoin_rate(currency):
    url = 'https://bitpay.com/api/rates'
    res = requests.get(url)
    if res.status_code != 200:
        return Response('ERROR: something went wrong', status=res.status_code)
    result = res.json()
    value = None
    for item in result:
        if item['code'] == currency:
            value = item['rate']
            break
    return str(value)


app.run(debug=True)
