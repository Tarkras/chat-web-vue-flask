import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# import json
from typing import Any

from flask import Flask, g, request
# from flask_cors import CORS

cred = credentials.Certificate('local/cred.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://chat-web-vue-flask-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference('/users')

app = Flask(__name__)

@app.route('/users')
def get_users():
    return ref.get()

@app.route('/')
def hello_world():
    return ref.get()

if __name__ == '__main__':
    app.run(debug=True)
