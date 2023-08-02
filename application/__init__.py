from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import secrets
from decouple import config

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
app.config['SECRET_KEY'] = secrets.token_hex(8)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from application import routes