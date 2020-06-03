from flask import Flask, request, render_template
from stories import *


app = Flask(__name__)

@app.route("/form")
def show_form():
    return render_template("form.html")

@app.route("/story")
def show_madlib():
    p =  request.args["place"]
    n = request.args["noun"]
    v = request.args["verb"]
    adj = request.args["adjective"]
    pl = request.args["plural_noun"]
    txt = story.generate({"place": p, "noun": n,"verb": v, "adjective": adj, "plural_noun": pl})
    return render_template("story.html", txt =txt)