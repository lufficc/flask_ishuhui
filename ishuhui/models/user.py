from flask import current_app
from flask_login import UserMixin


class User(UserMixin):
    def get_id(self):
        return '1'

    @property
    def name(self):
        return current_app.config['USERNAME']
