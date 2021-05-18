from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_message import Message
#from flask_app.controllers import controller_routes
    
@app.route('/login/send', methods=["POST"])
def send_message():
    is_valid = Message.validate_form(request.form)
    if not is_valid:
        return redirect('/login')
    print(request.form["which_form"])
    data = {
        "content" : request.form["content"],
        "recipient_id" : request.form["which_form"],
        "account_id" : session["user_id"]
    }
    print(data)
    new_message_id=Message.insert_one(data)
    return redirect('/login')

@app.route('/login/delete/<message_id>')
def delete_message(message_id):
    data = {
        "message_id" : message_id
    }
    Message.delete_one(data)
    return redirect('/login')
