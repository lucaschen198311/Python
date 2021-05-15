from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojo import Dojo

@app.route("/dojos")
def home():
    dojo_list = Dojo.get_all()
    print(dojo_list)
    return render_template("home.html", dojo_list = dojo_list)

@app.route("/dojos/add", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.insert_one(data)
    return redirect('/dojos')