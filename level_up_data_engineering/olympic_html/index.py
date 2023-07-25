from flask import Flask, render_template, request, jsonify
from collections import namedtuple
from distutils import debug
import string
import csv 
import re
# jinja tags

#safe - can be used to pass HTML as a variable in jinja.
#capitalize- capitalises the first letter of every tag.
#lower - makes every word lowercase.
#upper - makes every word uppercase
#title - capitalises the first letter in every word 
#trim
#striptags - strips any HTML tags from a vari

# variables can be called from the html document with {{ $VARIABLE }}ß
# logic statements can be called from the html document with {% $LOGIC %}

# to pass an input via the URL bar use /<$VARIABLE>/ for example to pass the variable "name" via the URL use "/<name>"

index = Flask(__name__)

with open("10k_race_times.txt", "rt") as file:
    content = file.read()


def extract_times(content):
    times = []
    for line in content.splitlines(): # splits the races variable into its individual lines so that each athlete is a seperate data set 
        match = re.search(r"\d{2}:\d{2}", line) 
        if match:
            clean = re.search(r"\d{2}:\d{2}", line) 
            times.append(clean.group()) # if the line matches then that line will be added to the matches dictionary
        else:
            next # if not the loop moves on with no actoin 
    return times

def extract_names(content):
    names = []
    name_pattern = re.compile(r'^[A-Za-z]+(?:\s[A-Za-z]+)*\s\d+$')
    for line in content.splitlines(): # splits the races variable into its individual lines so that each athlete is a seperate data set 
        print(line)
        match = re.findall(name_pattern, line)  
        print(match)
        if match:
            clean = re.findall(name_pattern, line)
            names.append(clean.group()) # if the line matches then that line will be added to the matches dictionary
        else:
            next # if not the loop moves on with no actoin 
    return names    


@index.route("/", methods=['GET', 'POST'])

def index_page():
    return render_template("index.html")


def get_medal(athlete):
    medals = []
    clean_medals = []
    count = 0

    for row in content.splitlines():
        if athlete in row:
            print(row)



    return medals

print(extract_names(content))

# Create custom error pages 



#@index.errorhandler(404)
#def page_not_found():
#    return render_template("404.html"), 404

#@index.errorhandler(500)
#def server_not_responding():
#    return render_template("500.html"), 500


#index.run(debug=True)