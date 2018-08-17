import os

DEBUG = False
SECRET_KEY='superuser'
# SQLALCHEMY_DATABASE_URI='postgresql://postgres:superuser@localhost/catalog_db' #
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False