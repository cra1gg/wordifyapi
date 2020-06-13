import flask
from flask import request, jsonify, render_template
import json
from flask import Flask
from flask_cors import CORS
from tinydb import TinyDB, Query



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app._static_folder = "templates/static/"
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")


# A route to return all of the available entries in our catalog.
@app.route('/word', methods=['GET'])
def api_all(): 
    db = TinyDB('wordify.json')
    cursor = Query()
    count = db.search(cursor.counter > 0)[0].get("counter")
    lst = []
    while len(lst) == 0:
        count = count + 1
        lst = db.get(doc_id=count)
    word = lst.get("word")
    print(word)
    db.remove(cursor.word == word)
    db.update({'counter': count}, cursor.counter > 0)
    returnlst = []
    returnlst.append(word)
    return jsonify(returnlst)
