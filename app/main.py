import flask
from flask import request, jsonify, render_template
import json
from flask import Flask
from flask_cors import CORS
from threading import Thread
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask('')
app._static_folder = "templates/static/"
CORS(app)
cred = credentials.Certificate("firebasecreds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://wordify-4eccd.firebaseio.com/"
})

def run():

  app.run(host='0.0.0.0',port=8080)

@app.route('/')
def home():
    return render_template("index.html")


# A route to return all of the available entries in our catalog.
@app.route('/word', methods=['GET'])
def api_all(): 
    ref = db.reference('/words')
    snapshot = ref.order_by_key().limit_to_first(1).get()
    res = list(snapshot.keys())[0] 
    word = snapshot.get(res).get("word")
    r = requests.get('https://jsonbox.io/box_12bd84a60a7e10896ec4/?q=s:' + word)
    while len(r.json()) > 0: 
        ref2 = db.reference('/words/' + str(res))
        ref2.delete()
        snapshot = ref.order_by_key().limit_to_first(1).get()
        res = list(snapshot.keys())[0] 
        word = snapshot.get(res).get("word")
        r = requests.get('https://jsonbox.io/box_12bd84a60a7e10896ec4/?q=s:' + word)
    returnlst = []
    returnlst.append(word)
    return jsonify(returnlst)

def keep_alive():  
    t = Thread(target=run)
    t.start()