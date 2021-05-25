from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_account import Account
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if "id" in session:
        return redirect("/login")
    else:
        return render_template("regist_login.html")

@app.route('/login')
def login_successs():
    if "id" not in session:
        return redirect("/")
    else:
        return render_template("success.html")

@app.route('/email_check', methods=["POST"])
def email_check():
    find = False
    data={
        "email": request.form["email"]
    }
    result=Account.get_account_by_email(data)
    if result:
        find=True
    return render_template("partial_emailcheck.html", find=find)
    
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
    session["id"] = new_account_id
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
    session["id"] = account[0]["id"]
    return redirect("/login")

@app.route('/namesearch')
def name_serach():
    data = {
        "first_name" : request.args.get('name') + "%"
    }
    print(data)
    name_list = Account.search_name(data)
    print(name_list)
    return render_template("name_search.html", name_list=name_list)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')