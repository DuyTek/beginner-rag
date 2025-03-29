from flask import Flask, jsonify
from error_handler import register_error_handlers

app = Flask(__name__)

register_error_handlers(app)


@app.get('/hello')
def hello_world():
    return jsonify({"message": "Hello, World!"})
