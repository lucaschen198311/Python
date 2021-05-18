from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_account import Account
#from flask_app.controllers import controller_routes
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
    
@app.route('/regist_validate', methods=['POST'])
def regist_validate():
    print("Got Post Info")
    print(request.form)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }
    account = Account.get_account_by_email(data)
    if len(account)>0:
        flash("Email has been used for registration already.", 'email')
        return redirect('/')
    
    if not Account.validate_regist(account, data):
        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(data["password"])
    data["password"] = pw_hash
    new_account_id = Account.insert_one(data)
    print(new_account_id)
    session["user_id"] = new_account_id
    session["first_name"] = data["first_name"]
    return redirect("/login")

@app.route('/login_validate', methods=['POST'])
def login_validate():
    data = {
        "email" : request.form["email"]
    }
    account = Account.get_account_by_email(data)
    print(account)
    if len(account)<1:
        flash("Email or password invalid." 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(account[0]["password"], request.form["password"]):
        flash("Email or password invalid." 'login')
        return redirect("/")
    session["user_id"] = account[0]["id"]
    session["first_name"] = account[0]["first_name"]
    return redirect("/login")