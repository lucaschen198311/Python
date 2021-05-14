from flask_app import app
from flask import render_template,redirect,request,session,flash
#from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route("/users")
def index():
    users = User.get_all()
    return render_template("user_curd.html", users = users)

@app.route("/users/new")
def create_user():
    return render_template("user_create_curd.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.insert_one(data)
    return redirect('/users')

@app.route("/users/<int:id>")
def show_user(id):
    user = User.get_one(id)
    print(user)
    return render_template("show_user_curd.html", user=user)

@app.route("/users/<int:id>/delete")
def delete_user(id):
    User.delete_one(id)
    return redirect('/users')

@app.route("/users/<int:id>/edit")
def edit_user(id):
    return render_template("user_edit_curd.html", user_id=id)

@app.route("/users/update/<int:id>", methods=['POST'])
def update_user(id):
    data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update_one(data)
    return redirect('/users')
