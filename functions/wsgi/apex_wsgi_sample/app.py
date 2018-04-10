# coding: utf-8

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<path:path>')
def any_path(path):
    return f'Here: <code>/{path}</code>'


if __name__ == '__main__':
    app.run()
