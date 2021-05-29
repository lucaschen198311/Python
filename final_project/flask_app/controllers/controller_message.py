from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_message import Message
from flask_app.models.model_account import Account

@app.route('/message/<message_id>')
def show_message(message_id):
    data = {
        "id" : message_id
    }
    message = Message.display_message(data)
    return render_template("display_message.html", message=message)

@app.route('/send_message/<sent_to_id>')
def send_message(sent_to_id):
    data = {
        "id" : sent_to_id
    }
    sent_to_username = Account.get_username_by_id(data)
    return render_template("send_message.html", sent_to_username=sent_to_username, sent_to_id=sent_to_id)

@app.route('/send_message/<sent_to_id>/message_validate', methods=['POST'])
def validate_message(sent_to_id):
    data = {
        "sent_to" : request.form["sent_to"],
        "content" : request.form["content"],
        "title" : request.form["title"],
        "account_id" : session["user_id"]
    }
    data1 ={
        "username" : request.form["sent_to"]
    }
    if not Message.validate_message(data):
        return redirect(f"/send_message/{sent_to_id}")
    elif len(Account.get_account_by_username(data1))!= 1:
        flash("username is invalid or doesn't exist.")
        return redirect(f"/send_message/{sent_to_id}")
    else:
        Message.send_message(data)
        return redirect("/dashboard")

@app.route('/message/<message_id>/delete')
def delete_message(message_id):
    data = {
        "id" : message_id
    }
    Message.delete_message(data)
    return redirect("/dashboard")
