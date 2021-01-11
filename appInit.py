from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.debug = True
app.config.from_object('config')
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)


