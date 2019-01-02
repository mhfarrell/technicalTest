import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app
import requests
import json
import sys, getopt, pprint
from pymongo import MongoClient

c = MongoClient('mongodb://admin:Admin123@ds119024.mlab.com:19024/cardatabase')
db= c.cardatabase
make = db.cars.distinct("Make")
model = db.cars.distinct("Short Model")
year = db.cars.distinct("Year introduced")
    
@app.route('/')
@app.route('/index')
def index():
    i=8
    results = db.cars.find().limit(i)
    print("finished")
    return render_template('index.html', title='Home', numresults=str(i), make=make, model=model, year=year, results=results)

@app.route('/search', methods=['GET', 'POST'])
def search():
    myQuery = {'Make':request.form.get('carMake'),'Short Model':request.form.get('carModel'),'Year introduced':request.form.get('carYear')}
    results = db.cars.find(myQuery)
    i=results.count()
    print("search finish")    
    return render_template('search.html', title='Search', numresults=str(i), make=make, model=model, year=year, results=results)
