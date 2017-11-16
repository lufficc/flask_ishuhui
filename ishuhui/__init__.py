from flask import Flask

from . import csrf


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
    from ishuhui.extensions.loginmanger import login_manager
    from ishuhui.extensions.flasksqlalchemy import db
    login_manager.setup_app(app)
    db.init_app(app)

    csrf.init(app)

    from ishuhui.logger import init_logger
    init_logger(app)

    from ishuhui.controllers.comic import bp_comic
    app.register_blueprint(bp_comic)

    from ishuhui.controllers.admin import bp_admin
    app.register_blueprint(bp_admin)

    from ishuhui.controllers.auth import bp_auth
    app.register_blueprint(bp_auth)

    from ishuhui.controllers.error import bp_error
    app.register_blueprint(bp_error)

    from ishuhui.schedulers.scheduler import init_scheduler
    init_scheduler(app)

    with app.app_context():
        db.create_all()
    return app
