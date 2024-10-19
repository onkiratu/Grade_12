from flask import render_template   
from Grade_12 import app

@app.route("/")
def index():
    return render_template("index.html")

 