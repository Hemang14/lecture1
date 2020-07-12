from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello World! Trying Headline via Python"
    return render_template("index3.html",headline=headline)

@app.route("/bye")
def bye():
    headline = "BUI BUI"
    return render_template("index3.html",headline=headline)
