# File name: contacts.py
# Author: B D S Aritra & Andrew Briden
# Description: Creates contact information of the shuttle drivers
# Date: 06.06.2023

from flask import Flask


app = Flask(__name__)

# Creates the contacts
@app.route('/',methods=['GET','POST'])
def getContacts():
    contacts = {
        'John Doe': {
            'Picture': 'https://randomuser.me/api/portraits/men/11.jpg',
            'Position': 'Shuttle Driver',
            'Contact': '+1 (555) 123-4567',
            'Email': 'john.doe@trincoll.edu'
        },
        'Jane Smith': {
            'Picture': 'https://randomuser.me/api/portraits/women/12.jpg',
            'Position': 'Shuttle Driver',
            'Contact': '+1 (555) 987-6543',
            'Email': 'jane.smith@trincoll.edu'
        },
        'Bob Johnson': {
            'Picture': 'https://randomuser.me/api/portraits/men/10.jpg',
            'Position': 'Shuttle Driver',
            'Contact': '+1 (555) 555-1212',
            'Email': 'bob.johnson@trincoll.edu'
        },
        'Tarek Alsolame': {
            'Picture': 'https://randomuser.me/api/portraits/men/15.jpg',
            'Position': 'Shuttle Driver',
            'Contact': '+1 (555) 555-1215',
            'Email': 'tarek.alsolame@trincoll.edu'
        },
        'Armen Nanayan': {
            'Picture': 'https://randomuser.me/api/portraits/men/16.jpg',
            'Position': 'Shuttle Driver',
            'Contact': '+1 (555) 555-1217',
            'Email': 'armen.nanayan@trincoll.edu'
        }
    }
    return contacts

# Contacts Microservice
if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=8092,debug=True)
