
from flask import Flask

app = Flask('wsgi_ex')

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"
