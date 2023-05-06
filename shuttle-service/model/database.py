# File name: database.py
# Author: B D S Aritra & Andrew Briden
# Description: Database Microservice to develop and access the database
# Date: 06.06.2023

import pymongo
from flask import Flask,jsonify
import os


# Connects to the database
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = os.environ['MONGODB']
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = pymongo.MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Location']

# Creates the database
def make_database():
  dbname = get_database()
  collection_name = dbname["Locationdb"]
  item_1 = {
    "location" : "Mather",
    "time" : "09:00",
  }
  item_2 = {
    "location" : "Seabury",
    "time" : "09:05",
  }
  item_3 = {
    "location" : "155 Allen Place",
    "time" : "09:15",
  }
  item_4 = {
    "location" : "Hillel House",
    "time" : "09:20",
  }
  item_5 = {
    "location" : "Broad Street",
    "time" : "09:25",
  }
  item_6 = {
    "location" : "Crescent Street Lot",
    "time" : "09:30",
  }
  item_7 = {
    "location" : "69 Crescent Street",
    "time" : "09:35",
  }
  item_8 = {
    "location" : "Hallden",
    "time" : "09:40",
  }
  item_9 = {
    "location" : "Raether LITC",
    "time" : "09:45",
  }
  item_10 = {
    "location" : "Ferris Broad Street Parking Lot",
    "time" : "09:50",
  }
  item_11 = {
    "location" : "Funston",
    "time" : "09:55",
  }
  item_12 = {
    "location" : "Mather",
    "time" : "10:00",
  }
  item_13 = {
    "location" : "Seabury",
    "time" : "10:05",
  }
  item_14 = {
    "location" : "155 Allen Place",
    "time" : "10:15",
  }
  item_15 = {
    "location" : "Hillel House",
    "time" : "10:20",
  }
  item_16 = {
    "location" : "Broad Street",
    "time" : "10:25",
  }
  item_17 = {
    "location" : "Crescent Street Lot",
    "time" : "10:30",
  }
  item_18 = {
    "location" : "69 Crescent Street",
    "time" : "10:35",
  }
  item_19 = {
    "location" : "Hallden",
    "time" : "10:40",
  }
  item_20 = {
    "location" : "Raether LITC",
    "time" : "10:45",
  }
  item_21 = {
    "location" : "Ferris Broad Street Parking Lot",
    "time" : "10:50",
  }
  item_22 = {
    "location" : "Funston",
    "time" : "10:55",
  }
  item_23 = {
    "location" : "Mather",
    "time" : "11:00",
  }
  item_24 = {
    "location" : "Seabury",
    "time" : "11:05",
  }
  item_25 = {
    "location" : "155 Allen Place",
    "time" : "11:15",
  }
  item_26 = {
    "location" : "Hillel House",
    "time" : "11:20",
  }
  item_27 = {
    "location" : "Broad Street",
    "time" : "11:25",
  }
  item_28 = {
    "location" : "Crescent Street Lot",
    "time" : "11:30",
  }
  item_29 = {
    "location" : "69 Crescent Street",
    "time" : "11:35",
  }
  item_30 = {
    "location" : "Hallden",
    "time" : "11:40",
  }
  item_31 = {
    "location" : "Raether LITC",
    "time" : "11:45",
  }
  item_32 = {
    "location" : "Ferris Broad Street Parking Lot",
    "time" : "11:50",
  }
  item_33 = {
    "location" : "Funston",
    "time" : "11:55",
  }
  item_33 = {
    "location" : "Mather",
    "time" : "12:00",
  }
  item_34 = {
    "location" : "Seabury",
    "time" : "12:05",
  }
  item_35 = {
    "location" : "155 Allen Place",
    "time" : "12:15",
  }
  item_36 = {
    "location" : "Hillel House",
    "time" : "12:20",
  }
  item_37 = {
    "location" : "Broad Street",
    "time" : "12:25",
  }
  item_38 = {
    "location" : "Crescent Street Lot",
    "time" : "12:30",
  }
  item_39 = {
    "location" : "69 Crescent Street",
    "time" : "12:35",
  }
  item_40 = {
    "location" : "Hallden",
    "time" : "12:40",
  }
  item_41 = {
    "location" : "Raether LITC",
    "time" : "12:45",
  }
  item_42 = {
    "location" : "Ferris Broad Street Parking Lot",
    "time" : "12:50",
  }
  item_43 = {
    "location" : "Funston",
    "time" : "12:55",
  }
  item_44 = {
    "location" : "Mather",
    "time" : "13:00",
  }
  if(collection_name.count_documents({})==0):
    collection_name.insert_many([item_1, item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11,item_12,item_13,item_14,item_15,
                              item_16, item_17,item_18,item_19,item_20,item_21,item_22,item_23,item_24,item_25,item_26,item_27,item_28,item_29,item_30,
                              item_31, item_32,item_33,item_34,item_35,item_36,item_37,item_38,item_39,item_40,item_41,item_42,item_43,item_44
                              ])
  item_details = collection_name.find()
  return item_details

# Converts the database into a readable format
def access_database():
  dbname = get_database()
  make_database()
  # Create a new collection
  collection_name = dbname["Locationdb"]  
  item_details = collection_name.find({},{"_id":0})
  return item_details


app = Flask(__name__)

# Returns the string version of the list in the database
@app.route('/')
def home():
   list_cur = list(access_database())
   return jsonify(list_cur)
    
# Database Microservice
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8085)
 

