from flask import jsonify, render_template, request
from pymongo import MongoClient
import requests
from flask import Flask
import os

app = Flask(__name__)

#return the home page of the shuttle service
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/routes', methods=['GET', 'POST']) 
def getLocationDetails():
    return render_template("directions.html")

# Connect to the MongoDB database
client = MongoClient('mongodb://mongodb-service:27017/')
db = client['Location']
collection = db['Locationdb']

# Define a route to display the data in an HTML table
@app.route('/schedule', methods=['GET', 'POST'])
def display_table():
    # Retrieve the data from the database
    data = []
    for document in collection.find():
        data.append({'location': document['location'], 'time': document['time']})
    # Render the data in an HTML table
    return render_template('schedule.html', data=data)

#Gets the first page of requesting the shuttle
@app.route('/requestShuttle', methods=['GET', 'POST']) 
def index():
    time = requests.get(os.environ['REAL_TIME'])
    return render_template('request.html',current_time = time.text,)

#Gets the location of the shuttle and the arrival time
@app.route('/get_location', methods=['GET', 'POST'])
def get_location():
    location = request.form['location']
    headers = {'Content-Type': 'application/json'}
    sendlocation = requests.post(os.environ['REQUEST_SHUTTLE'],json=location,headers = headers)
    timeresponse = requests.get(os.environ['REAL_TIME_TRACKING'])
    return render_template('request.html', message = sendlocation.text, realtime = timeresponse.text)

#Produces the contacts of the shuttle drivers
@app.route('/getContacts', methods=['GET', 'POST']) 
def contacts():
    getContacts = requests.get(os.environ['CONTACTS']).json()
    return render_template('contacts.html', contacts=getContacts)



# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8089,debug=True)

