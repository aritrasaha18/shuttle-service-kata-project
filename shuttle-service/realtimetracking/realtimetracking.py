# File name: realtimetracking.py
# Author: B D S Aritra & Andrew Briden
# Description: Generates the real-time tracking of the shuttle service
# Date: 06.06.2023

from flask import Flask, request,json
import requests
import os

# Real-time trakcing of the shuttle service
def realtimetracking(input,database):
    hours, minutes = input.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Calculate the nearest 5 minutes
    nearest_five = round(minutes / 5) * 5

    # If the nearest five is 60, adjust the hours and set minutes to 0
    if nearest_five == 60:
        hours += 1
        minutes = 0
    else:
        minutes = nearest_five

    # Format the time with leading zeroes if necessary
    formatted_hours = "{:02d}".format(hours)
    formatted_minutes = "{:02d}".format(minutes)

    realtime = f"{formatted_hours}:{formatted_minutes}"
    data = database
    row_time=[]
    row_location=[]
    for item in data:
        row_time.append((item["time"]))
        row_location.append((item["location"]))
    count = 0
    for row in row_time:
        if(row==realtime):
            return "The shuttle is currently near "+row_location[count]+'.'
        count=count+1
    return "The shuttle is currently not running!"

real = Flask(__name__)

# Routing to get response from other microservice
@real.route('/time', methods=['GET'])
def home():
   database = (requests.get(os.environ['DATABASE_DB'])).json()
   time = requests.get(os.environ['REAL_TIME']).text
   return realtimetracking(time,database)   


# realtimetracking Microservice
if __name__ == '__main__':
    real.run(host="0.0.0.0", port=8087)