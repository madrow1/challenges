from distutils.log import debug
# This has to be installed with pip install flask 
from flask import Flask

# This is required, it creates a Flask object, it is case sensetive 
app = Flask(__name__)

# THis initialises the app route 
@app.route("/")

def hello():
    return "Hello, world"

# When the app is run this will create a simple server on your localhost 
app.run(debug=True)

