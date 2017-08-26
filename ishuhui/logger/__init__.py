import logging
from logging.handlers import RotatingFileHandler


def init_logger(app):
    handler = RotatingFileHandler('logs/ishuhui.log', maxBytes=1024 * 1024 * 2, backupCount=2)
    handler.setLevel(logging.INFO)
    logging_format = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
