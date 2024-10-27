from flask import render_template

from mod import app

@app.route('/')
def test():
    return 'Hellow World!'

@app.route("/indexhtml")
def index():
    return render_template("index.html", insert_something = "del")

@app.route("/page2")
def page2():
    contents = {"content1": "content1",
                "content2": "content2"}
    return render_template("page2.html", insert_something = contents)