from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, This is a python-dev docker from wucharles!'