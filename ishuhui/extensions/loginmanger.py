from flask_login import LoginManager

from ..models.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User()
