import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = '\xba\xf5\xa6\x076\xe4\x9eb\x10\x8bZpV\x13:\xfey\xfc\x9a\xc4\x82A\x7f\xe2'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)

import models
import views
