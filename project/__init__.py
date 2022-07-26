from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask("project")
app.config['SECRET_KEY'] = os.urandom(32)

from project.controllers import *
