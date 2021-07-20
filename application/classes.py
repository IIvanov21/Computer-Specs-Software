from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
#Database classes based on the ERD diagram
class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyType = db.Column(db.String(10),nullable=False)
    make = db.Column(db.String(60),nullable=False)
    model = db.column(db.String(60), nullable=False)
    series = db.column(db.String(60), nullable=False)
    cpus = db.relationship('CPU', backref='motherboard')
    case = db.relationship('Case', backref='motherboard')
    
class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(10),nullable=False)
    series = db.column(db.String(10), nullable=False)
    model= db.column(db.String(20), nullable=False)
    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.id'), nullable = False)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyType = db.Column(db.String(10),nullable=False)
    make = db.Column(db.String(60),nullable=False)
    model= db.column(db.String(60), nullable=False)
    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.id'), nullable = False)

class CreateCPUEntry(FlaskForm):
    make = SelectField("CPU Manufacturer:",choices=[("AMD","AMD"),("Intel","Intel")])
    series = StringField("CPU Series:")
    model = StringField("CPU Model: ")

class CreateCaseEntry(FlaskForm):
    keyType = SelectField("Case Type: ", choices=[("XL-ATX","XL-ATX"),("EATX","EATX"),("ATX","ATX"),("mATX/ITX","mATX/ITX"),("MINI-ITX","MINI-ITX")])
    make = StringField("Case Manufacturer: ")
    model = StringField("Case Model:")

class CreateMotherBoardEntry(FlaskForm):
    keyType = SelectField("Motherboard Type: ", choices=[("XL-ATX","XL-ATX"),("EATX","EATX"),("ATX","ATX"),("mATX/ITX","mATX/ITX"),("MINI-ITX","MINI-ITX")])
    make = SelectField("Motheraboard Manufacturer:",choices=[("Asus","Asus"),("Aourus","Aourus"),("MSI","MSI"),("ASRock","ASRock")])
    model = StringField("Motherboard Model: ")
    series = StringField("Motherboard Series:")
    submit = SubmitField('Confirm')

