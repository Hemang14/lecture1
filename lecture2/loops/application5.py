 from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    names = ["Un","Arianne","Lurline","Ebony","Carolin","Lisandra","Leia","Terrence","Randell","Cassaundra","Christina",
              "Le","Zandra","Dessie","Allyson","Krystina","Christopher","Latina","Cleotilde","Maryland"]
    return render_template("index5.html",names=names)
