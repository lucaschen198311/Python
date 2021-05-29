from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_pypie import Pypie

@app.route('/dashboard/add', methods=["POST"])
def add_pypie():
    print(request.form)
    is_valid = Pypie.validate_form(request.form)
    if not is_valid:
        return redirect('/dashboard')
    data = {
        "name" : request.form["name"],
        "filling" : request.form["filling"],
        "crust" : request.form["crust"],
        "account_id" : session["user_id"]
    }
    print(data)
    Pypie.insert_one(data)
    return redirect('/dashboard')

@app.route('/edit/<pypie_id>')
def show_edit_pypie(pypie_id):
    data = {
        "pypie_id" : pypie_id
    }
    session["pypie_id"] = pypie_id
    pypie = Pypie.get_pypie_by_id(data)
    print(session["user_id"])
    return render_template("edit_pypie.html", pypie=pypie)

@app.route('/pypie/update', methods=["POST"])
def update_recipe():
    is_valid = Pypie.validate_form(request.form)
    if not is_valid:
        return redirect(f"/edit/{session['pypie_id']}")
    data = {
        "id" : session["pypie_id"],
        "name" : request.form["name"],
        "filling" : request.form["filling"],
        "crust" : request.form["crust"]
    }
    Pypie.update_one(data)
    return redirect('/dashboard')

@app.route('/dashboard/delete/<pypie_id>')
def delete_pypie(pypie_id):
    data = {
        "pypie_id" : pypie_id
    }
    Pypie.delete_one(data)
    return redirect('/dashboard')

@app.route('/pies')
def pypie_derby():
    print(session["user_id"])
    all_pypies = Pypie.get_all_pies()
    return render_template("pypies.html", all_pypies=all_pypies)

@app.route('/show/<pypie_id>')
def show_recipe(pypie_id):
    data = {
        "pypie_id" : pypie_id
    }
    name = Pypie.get_account_name_by_pypieid(data)
    print(name)
    session["pypie_id"] = pypie_id
    session["name"] = name[0]
    pypie = Pypie.get_pypie_by_id(data)
    print(session["user_id"])
    return render_template("show_pypie.html", pypie=pypie, name=session["name"])

@app.route('/vote')
def vote_pypie():
    data={
        "pypie_id" : session["pypie_id"]
    }
    Pypie.vote(data)
    return redirect('/pies')