from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_account import Account
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/regist')
def regist():
    return render_template("registration.html")
    
@app.route('/regist_validate', methods=['POST'])
def regist_validate():
    print("Got Post Info")
    print(request.form)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "username"  : request.form["username"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }
    account = Account.get_account_by_username(data)
    if len(account)>0:
        flash("Username has been used for registration already, please choose a unique one.")
        return redirect('/regist')
    
    if not Account.validate_regist(data):
        return redirect("/regist")
    
    pw_hash = bcrypt.generate_password_hash(data["password"])
    data["password"] = pw_hash
    new_account_id = Account.insert_one(data)
    print(new_account_id)
    session["user_id"] = new_account_id
    session["username"] = data["username"]
    return redirect("/dashboard")

@app.route('/login_validate', methods=['POST'])
def login_validate():
    data = {
        "username" : request.form["username"]
    }
    account = Account.get_account_by_username(data)
    print(account)
    if len(account)<1:
        flash("Username or password invalid.")
        return redirect("/login")
    if not bcrypt.check_password_hash(account[0]["password"], request.form["password"]):
        flash("Username or password invalid." 'login')
        return redirect("/login")
    session["user_id"] = account[0]["id"]
    session["username"] = account[0]["username"]
    return redirect("/dashboard")