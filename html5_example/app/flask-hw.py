#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return b'Hello World!'

if __name__ == '__main__':
    app.run()
