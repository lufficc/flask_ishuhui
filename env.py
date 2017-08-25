import os
APP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/ishuhui'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
SQLALCHEMY_DATABASE_URI='sqlite:///' + APP_PATH + '/tmp/ishuhui.db'

USERNAME='lufficc'
PASSWORD='123456'