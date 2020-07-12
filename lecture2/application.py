from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
@app.route("/hemang")
def hemang():
    return "Hello Hemang!"
@app.route("/astono")
def astono():
    return "Hello Astono!"
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
