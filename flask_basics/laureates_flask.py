from flask import Flask, render_template, jsonify, request
import csv
from distutils.log import debug 
app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f: 
    reader = csv.DictReader(f)
    laureates = list(reader)

#index calls the laureates route and renders it out in browser
@app.route("/")
def index():
    return render_template("laureates.html")

# jsonify here is used to convert the csv formatted files to json
@app.route("/laureates/")
#def laureate():
#    return jsonify(laureates)

def laureate_list():
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    search_string = request.args.get("surname").lower().strip()

    for laureate in laureates:
        if search_string in laureate["surname"].lower():
           results.append(laureate)
    return jsonify(results)

app.run(debug=True) 