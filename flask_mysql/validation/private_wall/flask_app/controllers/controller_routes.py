from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_account import Account
from flask_app.models.model_message import Message

@app.route('/')
def index():
    if "user_id" in session:
        return redirect("/login")
    else:
        return render_template("regist_login.html")

@app.route('/login')
def login_successs():
    if "user_id" not in session:
        return redirect("/")
    else:
        data = {
            "id" : session["user_id"]
        }
        messages = Message.get_message_to_account(data)
        print(messages)
        account_list = Account.get_account_exclude_id(data)
        print(account_list)
        total_sent = Message.total_message_sent(data)
        print(total_sent)
        total_received = Message.total_message_received(data)
        print(total_received)
        return render_template("private_wall.html", messages=messages, account_list=account_list, first_name=session["first_name"], total_sent=total_sent, total_received=total_received)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')