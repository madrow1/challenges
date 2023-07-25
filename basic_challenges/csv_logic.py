# Import the csv and other modules
import csv
from datetime import datetime
from pprint import pprint
import json

# It is possible to store data as a CSV inside of a python script, like the below
# However for readability it is  better to import it programatically
EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

# This is a python dictionary, made up of keys on the left, and strings on the right, both of these can be a number technically
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# This opens the file laureates.csv, the "r" means that the file has been opened as readonly 
# The csv.DictReader method reads each line of a CSV file into the variable "reader" for each loop the 
# variable "reader" is then saved into the laureates variable. f could be anything
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# This for loop then performs a simple lookup on the CSV, matching the key "surname" to the data "Zeeman"
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        # String added here to make it look pretty, no otherreasons 
        print("=====================")
        # datetime creates structures to format dates using the unix datetime format
        # the strptime method interprets a string to create a date formatted object, in this case we tell it to convert
        # a string from the year of birth to a variable date.
        year_date = datetime.strptime(laureate["year"], "%Y")
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        print("age", year_date.year - born_date.year)
        print("=====================")
        break

# To convert a CSV to a string use the below method
einstein_json = json.dumps(EINSTEIN)
pprint(einstein_json)
print("============================")

# To convert a json to a dictionary reverse it with the .loads() method
back_to_dict = json.loads(einstein_json)
pprint(back_to_dict)

# Reading a large CSV file into json format is basically the same as reading it into a dictionary
# the "f" is arbitrary, and is used to represent a file object, it could be anything
with open("laureates.csv", "r") as f: 
    # This reads the CSV file into a python dictionary
    reader = csv.DictReader(f)
    # This creates a list based on that dictionary
    laureate = list(reader)

# The file laureate.json does not exist yet, the "w" means that python will write to this file.
with open("laureate.json", "w") as f:
    json.dump(laureates, f, indent=2)