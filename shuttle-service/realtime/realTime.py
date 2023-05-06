# File name: realTime.py
# Author: B D S Aritra & Andrew Briden
# Description: Generates a time between (9:00 pm and 1:00 am)
# Date: 06.06.2023

import random
from flask import Flask

#Generates a random time between the running service hours
def realTime():
    hours = random.randint(9, 12)   # generate random hour between 9 and 12
    minutes = random.randint(0, 59) # generate random minute between 0 and 59
    return f"{hours:02d}:{minutes:02d}" # format time as "hh:mm"


real = Flask(__name__)

# Routing for communication
@real.route('/')
def home():
   return realTime()



# realtime Microservice
if __name__ == '__main__':
    real.run(host="0.0.0.0", port=8086)
