from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/table')
def display_table():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    for user in users:
        user["full_name"] = user["first_name"] + " " + user["last_name"]
    return render_template("table.html", col_head =["First Name", "Last Name", "Full Name"], users = users)


@app.errorhandler(Exception)
def server_error(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)