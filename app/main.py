import flask
from flask import request, jsonify, render_template
import json
from flask import Flask
from flask_cors import CORS


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
    f = open("output.txt", "r")
    lst = f.readlines()
    returnlst = []
    returnlst.append(lst.pop(0).rstrip("\n"))
    f2 = open("output.txt", "w")
    f2.writelines(lst)
    return jsonify(returnlst)
