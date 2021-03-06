# tutorial from
# https://code.visualstudio.com/docs/python/tutorial-flask#_go-to-definition-and-peek-definition-commands

from flask import Flask
from flask import render_template
from datetime import datetime
import re

# TO INIT THE FLASK PROJECT RUN
# python -m flask run

print("Execute: python -m flask run")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

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
    