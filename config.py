import os

basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_BASE="http://localhost"
UPLOAD_FOLDER = basedir+'/app/static/uploads'
ALLOWED_EXTENSIONS = set(['csv'])
MAX_CONTENT_LENGTH = 1 * 1024 * 1024

CRSF_ENABLED = True
#put secret key here
SECRET_KEY= ''
#put uri here
SQLALCHEMY_DATABASE_URI=''
SQLALCHEMY_TRACK_MODIFICATIONS = False
