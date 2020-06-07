import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/word', methods=['GET'])
def api_all(): 
    f = open("output.txt", "r")
    lst = f.readlines()
    returnlst = []
    returnlst.append(lst.pop(0).rstrip("\n"))
    f2 = open("output.txt", "w")
    f2.writelines(lst)
    return json.dumps(returnlst)
