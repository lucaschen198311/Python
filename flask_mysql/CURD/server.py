from flask import Flask, render_template, request, session, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')
    friends = mysql.query_db('SELECT * FROM friends;')
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/form")
def submit_form():
    return render_template("index_form.html")

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    mysql = connectToMySQL('first_flask')
    query="INSERT INTO friends (first_name, last_name, occupation) VALUES(%(fn)s, %(ln)s, %(occupation)s);"
    data ={"fn": request.form["fname"], "ln": request.form["lname"], "occupation": request.form["occ"]}
    new_id = mysql.query_db(query, data)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
    
