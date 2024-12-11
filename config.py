import os

secret_key = '1234'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/databases/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False