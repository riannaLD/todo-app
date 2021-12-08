from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = str(uuid.uuid4()) #generate a random secret key for the app to start

db = SQLAlchemy(app)

from application import routes