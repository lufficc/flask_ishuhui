import os
APP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/ishuhui'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
SQLALCHEMY_DATABASE_URI='sqlite:///' + APP_PATH + '/tmp/ishuhui.db'
SECRET_KEY='7c401a1e5fd54c6cd8cd0d5016c2911157a6127815ab7686'
USERNAME='lufficc'
PASSWORD='123456'
ENABLE_CELERY=True
CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
