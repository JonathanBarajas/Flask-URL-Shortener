import os

DB_USERNAME = 'z'
DB_PASSWORD = 'potato6'
DB_DATABASE_NAME = 'shortener'
#DB_HOST = os.getenv('IP', '172.19.0.2')
DB_HOST = 'db'
APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'password'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE_NAME)
STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
RECAPTCHA_PUBLIC_KEY = '<Your own keys from Google>'
RECAPTCHA_PRIVATE_KEY = '<You can get these keys at https://www.google.com/recaptcha/admin>'
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
SERVER_NAME = 'localhost:9009'
# SERVER_NAME = 'YourDomain.com'

