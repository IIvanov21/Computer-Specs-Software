from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
#Database classes based on the ERD diagram
class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    cpus = db.relationship('CPU', backref='build')
    case = db.relationship('ComputerCase', backref='build')
    motherboard = db.relationship('Motherboard', backref='build')

class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyType = db.Column(db.String(10),nullable=False)
    make = db.Column(db.String(60),nullable=False)
    model = db.Column(db.String(60), nullable=False)
    series = db.Column(db.String(60), nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'), nullable = False)

class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(10),nullable=False)
    series = db.Column(db.String(10), nullable=False)
    model= db.Column(db.String(20), nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'), nullable = False)

class ComputerCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyType = db.Column(db.String(10),nullable=False)
    make = db.Column(db.String(60),nullable=False)
    model= db.Column(db.String(60), nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'), nullable = False)
    submit = SubmitField('Confirm')


class CreateCPUEntry(FlaskForm):
    build_name = StringField("Build name:",validators=[DataRequired()])
    make = SelectField("CPU Manufacturer:",choices=[("AMD","AMD"),("Intel","Intel")])
    series = StringField("CPU Series:",validators=[DataRequired()])
    model = StringField("CPU Model: ",validators=[DataRequired()])
    submit = SubmitField('Confirm')


class CreateCaseEntry(FlaskForm):
    build_name = StringField("Build name:",validators=[DataRequired()])
    keyType = SelectField("Case Type: ", choices=[("XL-ATX","XL-ATX"),("EATX","EATX"),("ATX","ATX"),("mATX/ITX","mATX/ITX"),("MINI-ITX","MINI-ITX")])
    make = StringField("Case Manufacturer: ",validators=[DataRequired()])
    model = StringField("Case Model:",validators=[DataRequired()])
    submit = SubmitField('Confirm')


class CreateMotherBoardEntry(FlaskForm):
    build_name = StringField("Build name:",validators=[DataRequired()])
    keyType = SelectField("Motherboard Type: ", choices=[("XL-ATX","XL-ATX"),("EATX","EATX"),("ATX","ATX"),("mATX/ITX","mATX/ITX"),("MINI-ITX","MINI-ITX")])
    make = SelectField("Motheraboard Manufacturer:",choices=[("Asus","Asus"),("Aourus","Aourus"),("MSI","MSI"),("ASRock","ASRock")])
    model = StringField("Motherboard Model: ",validators=[DataRequired()])
    series = StringField("Motherboard Series:",validators=[DataRequired()])
    submit = SubmitField('Confirm')

class CreateBuildEntry(FlaskForm):
    name = StringField("Build name:",validators=[DataRequired()])
    submit = SubmitField('Confirm')

class ReadBuildEntry(FlaskForm):
    build_name = StringField("Build name:",validators=[DataRequired()])
    submit = SubmitField('Confirm')
    mb_name = StringField("Motherboard name:")
    cpu_name = StringField("CPU name:")
    case_name = StringField("Case name:")

class UpdateBuildEntry(FlaskForm):
    build_name = StringField("Build name:",validators=[DataRequired()])
    submit = SubmitField('Confirm')
    mb_name = StringField("Motherboard name:")
    upmb_name = StringField("Motherboard name:",validators=[DataRequired()])
    cpu_name = StringField("CPU name:")
    upcpu_name = StringField("CPU name:",validators=[DataRequired()])
    case_name = StringField("Case name:")
    upcase_name = StringField("Case name:",validators=[DataRequired()])      
