import datetime
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month==1 and now.date ==1
    return render_template("index4.html",new_year=new_year)
