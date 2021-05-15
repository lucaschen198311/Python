from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

@app.route("/ninjas")
def new_ninjas():
    dojo_list = Dojo.get_all()
    print(dojo_list)
    return render_template("new_ninjas.html", dojo_list = dojo_list)

@app.route("/ninjas/add", methods=["POST"])
def add_ninjas():
    name = request.form["dojo_select"]
    print(name)
    id = Dojo.get_id(name)
    print(id)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": id[0]['id']
    }
    Ninja.insert_one(data)
    return redirect('/ninjas')

@app.route("/dojos/<int:dojo_id>")
def show_ninjas(dojo_id):
    data = {
        "id" : dojo_id
    }
    dojo_ninja_join=Ninja.ninja_dojo_join(data)
    print(dojo_ninja_join)
    return render_template("show_ninja.html", dojo_ninja_join=dojo_ninja_join)