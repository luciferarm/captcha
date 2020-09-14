from webstky import webstky
from flask import render_template

@webstky.route("/")
def index():
    return render_template("index.html")
