# File name: requestShuttle.py
# Author: B D S Aritra & Andrew Briden
# Description: Generates the arrival time and location of the shuttle
# Date: 06.06.2023

import requests
from flask import Flask, jsonify, request
import os

# Returns the arrival time and location of the shuttle
def arrivalTime(location,data,currentTime):
    locationTimes = []
    for item in data:
        locationTimes.append(item["time"])
    if(int(currentTime[0:2])>13 or int(currentTime[0:2])<9):
            return "Sorry, The shuttle service is not running at this moment."
    for item in data:
        if(convertKey(currentTime)<=convertKey(item["time"]) and item["location"]==location):
            remaining = convertKey(item["time"])-convertKey(currentTime)
            if(remaining==0):
                return("Arriving now!")
            if(remaining==1):
                return('Arriving at '+location+' in '+str(remaining)+' minute.')
            if(remaining==60):
                return('Arriving at '+location+' in '+str(remaining)+' hour.')
            else:
                hour = remaining//60
                minutes = remaining%60
                if(minutes>0):
                    return('Arriving at '+location+' in '+str(remaining)+' minutes.')
                else:
                    return('Arriving in '+str(hour)+' hour ')
    return "Sorry, The shuttle service is not running at this moment."

# Produces key for the arrival times
def convertKey(input):
    bias = 0
    if(input[0:2]=="09"):
        bias = 0
    if(input[0:2]=="10"):
        bias = 1
    if(input[0:2]=="11"):
        bias = 2
    if(input[0:2]=="12"):
        bias = 3
    if(input[0:2]=="13"):
        bias = 4
    return(bias*60+int(input[3:5]))   



app = Flask(__name__)

# Routing to get response from other microservices
@app.route('/location', methods=['GET','POST'])
def home():
   location = request.get_json()
   database = (requests.get(os.environ['DATABASE_DB'])).json()
   time = requests.get(os.environ['REAL_TIME']).text
   return arrivalTime(location,database,time)



# requestshuttle Microservice
if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=8081,debug=True)