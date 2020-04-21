from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is my first web app made with Python and Flask hihi"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/hello2/<name>")
def hello_there2(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at - - -  %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello " + clean_name + "!Its: " + formatted_now
    return content
    