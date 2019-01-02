import os
import csv
import json
import requests
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open(os.path.join(sys.path[0], "resources\Vehicles.csv"), "r")
reader = csv.DictReader( csvfile )

c = MongoClient('mongodb://admin:Admin123@ds119024.mlab.com:19024/cardatabase')
db= c.cardatabase
if db.cars.find().count() > 0:
    print("Database populated")
else:
    db.cars.drop()
    header= [ "Vehicle ID", "Make", "Short Model", "Long Model", "Trim", "Derivative", "Year introduced", "Year discontinued", "Currently Available"]

    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]

        db.cars.insert(row)

    for x in db.cars.find():
        r = requests.get('https://izrite.com:5555/image/' + x['Vehicle ID'])
        r=r.json()
        db.cars.update_one({'Vehicle ID': x['Vehicle ID']},{'$set':{'Vehicle Image':r['url']}}, upsert=False)

    print("Database Updated")
