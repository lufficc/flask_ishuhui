import binascii
import os

from flask import session


def init(app):
    def generate_csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
        return session['_csrf_token']

    app.jinja_env.globals['csrf_token'] = generate_csrf_token
