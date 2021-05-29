from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_pypie import Pypie

@app.route('/')
def index():
    if "user_id" in session:
        return redirect("/dashboard")
    else:
        return render_template("regist_login.html")

@app.route('/dashboard')
def login_successs():
    if "user_id" not in session:
        return redirect("/")
    else:
        data = {
            "id" : session["user_id"]
        }
    pypies = Pypie.get_pypie_by_account(data)
    print(pypies)
    return render_template("dashboard.html", pypies=pypies, first_name=session["first_name"])
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')