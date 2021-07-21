from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask import Flask, render_template, request
from wtforms import SubmitField
from application import app, db
from application.classes import Motherboard,CPU,ComputerCase
from application.classes import CreateCaseEntry,CreateCPUEntry,CreateMotherBoardEntry

@app.route('/add',methods=['GET','POST'])
def add():   
    motherboard_form=CreateMotherBoardEntry()
    cpu_form=CreateCPUEntry()

    return render_template('addLayout.html',motherboard_form=motherboard_form,cpu_form=cpu_form)

@app.route('/add/motherboard',methods=['GET','POST'])
def addMotherboard():
    motherboard_form=CreateMotherBoardEntry()
    error=""

    if request.method=="POST":
        #Motherboard Entry configuration:
        motherboard_name=motherboard_form.name.data
        motherboard_keyType=motherboard_form.keyType.data
        motherboard_make=motherboard_form.make.data
        motherboard_model=motherboard_form.model.data
        motherboard_series=motherboard_form.series.data
  
        #If all checks have passed commit entries to the databses:
        if  motherboard_form.validate():
            new_motherboard_entry=Motherboard(name=motherboard_name,keyType=motherboard_keyType,make=motherboard_make,model=motherboard_model,series=motherboard_series)
            db.session.add(new_motherboard_entry)
            db.session.commit()

            return 'Added the new build entry!'
        else: return 'Failed to submit!'
    return render_template('addMotherboard.html',motherboard_form=motherboard_form,message=error)

@app.route('/add/cpu',methods=['GET','POST'])
def addCPU():
    cpu_form=CreateCPUEntry()
    error=""
    if request.method=="POST":
        #CPU Entry configuration:
        cpu_make=cpu_form.make.data
        cpu_series=cpu_form.series.data
        cpu_model=cpu_form.model.data
        if cpu_form.validate():
            new_cpu_entry=CPU(make=cpu_make,series=cpu_series,model=cpu_model,motherboard=Motherboard.query.filter_by(name=motherboard_name).first())
            db.session.add(new_cpu_entry)
            db.session.commit()
            return "Added a CPU!"
        else: return "Failed to add a CPU!"
    return render_template('addCPU.html',cpu_form=cpu_form,message=error)

@app.route('/add/case',methods=['GET','POST'])
def addCase():
    #Case Entry configuration:
    error=""
    if request.method=="POST":

        case_form=CreateCaseEntry()
        case_keyType=case_form.keyType.data
        case_make=case_form.make.data
        case_model=case_form.model.data

        if case_form.validate():
            new_case_entry=ComputerCase(keyType=case_keyType,make=case_make,model=case_model,motherboard=Motherboard.query.filter_by(name=motherboard_name).first())
            db.session.add(new_case_entry)
            db.session.commit()
            return "Added a Case!"
        else: 
            return "Failed to add a Case!"
    return render_template('addCase.html',case_form=case_form,message=error)    


@app.route('/',methods=['GET','POST'])
@app.route('/read',methods=['GET','POST'])
def read():
    cpu_form=CreateCPUEntry()
    case_form=CreateCaseEntry()
    motherboard_form=CreateMotherBoardEntry()

    mblist=[]
    teststring=''
    mbdata=Motherboard().query.all()
    cpudata=CPU().query.all()
    casedata=Case().query.all()
    teststring+="<h1>Motherboard</h1> "
    for data in mbdata:
        teststring+="<br>"+ str(data.id) + " " + data.name + " " + data.keyType + " " + data.make + " " + data.model + " " + data.series + "<br>"
    teststring+="<h1>CPU</h1> "
    for data in cpudata:
        teststring+="<br>"+ str(data.id) + " " +   data.make + " " + data.model + " " + data.series + "<br>"
    teststring+="<h1>Case</h1> "
    
    for data in casedata:
        teststring+="<br>"+ str(data.id) + " " +   data.make + " " + data.model + " " + data.keyType + "<br>"
   
    return teststring
