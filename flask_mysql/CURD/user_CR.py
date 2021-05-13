from flask import Flask, render_template, request, session, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('users')
    query = 'SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%M %d %Y") AS created_at FROM users;'
    users = mysql.query_db(query)
    print(users)
    return render_template("user_cr.html", users = users)

@app.route("/users/new")
def create_user():
    return render_template("user_create.html")

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
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    
