from flask import Flask, render_template, request, session, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('users')
    query = 'SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%M %d %Y") AS created_at FROM users;'
    users = mysql.query_db(query)
    print(users)
    return render_template("user_curd.html", users = users)

@app.route("/users/new")
def create_user():
    return render_template("user_create_curd.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    mysql = connectToMySQL('users')
    query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    new_id = mysql.query_db(query, data)
    return redirect('/users')

@app.route("/users/<int:id>")
def show_user(id):
    mysql = connectToMySQL('users')
    query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id=%(id)s;"
    data = {
        "id" : id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("show_user_curd.html", user=user[0])

@app.route("/users/<int:id>/delete")
def delete_user(id):
    mysql = connectToMySQL('users')
    query = 'DELETE FROM users WHERE id=%(id)s'
    data = {
        "id" : id
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route("/users/<int:id>/edit")
def edit_user(id):
    return render_template("user_edit_curd.html", user_id=id)

@app.route("/users/update/<int:id>", methods=['POST'])
def update_user(id):
    mysql = connectToMySQL('users')
    query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;'
    data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
    
