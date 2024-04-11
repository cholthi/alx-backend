#!/usr/bin/env python3
"""Basic flask app which renders a template"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """index view"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000)
