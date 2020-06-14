import flask
from flask import request, jsonify, render_template
import json
from flask import Flask
from flask_cors import CORS
from tinydb import TinyDB, Query
from threading import Thread


app = Flask('')
app._static_folder = "templates/static/"
CORS(app)

def run():
  app.run(host='0.0.0.0',port=8080)

@app.route('/')
def home():
    return render_template("index.html")


# A route to return all of the available entries in our catalog.
@app.route('/word', methods=['GET'])
def api_all(): 
    db = TinyDB('app/wordify.json')
    cursor = Query()
    count = db.search(cursor.counter > 0)[0].get("counter")
    lst = []
    while len(lst) == 0:
        count = count + 1
        lst = db.get(doc_id=count)
    word = lst.get("word")
    db.remove(cursor.word == word)
    db.update({'counter': count}, cursor.counter > 0)
    returnlst = []
    returnlst.append(word)
    return jsonify(returnlst)

def keep_alive():  
    t = Thread(target=run)
    t.start()