import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = str(os.environ.get('SECRET_KEY'))
    MAIL_SERVER = str(os.environ.get('MAIL_SERVER'))
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USERNAME = str(os.environ.get('MAIL_USERNAME'))
    MAIL_PASSWORD = str(os.environ.get('MAIL_PASSWORD'))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
