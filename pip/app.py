#  Copyright (c) 2022. Code by Dimitri AIGLE

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"