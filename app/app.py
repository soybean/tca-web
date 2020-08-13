import logging

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception('500 error')
    return 'An internal error occurred.', 500
