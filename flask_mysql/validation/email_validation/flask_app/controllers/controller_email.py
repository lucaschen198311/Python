from flask_app import app
import re
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_email import Email

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    return render_template("email_validate.html")
    
@app.route('/email_validate', methods=['POST'])
def validate_email():
    print("Got Post Info")
    print(request.form)
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email cannot be blank and must be in correct format.", 'email')
        return redirect("/")
    data = {
        "email" : request.form["email"]
    }
    email_exist = Email.validate_email(data)
    if not Email.validate_form(email_exist, data):
        return redirect("/")
    Email.insert_one(data)
    email_list = Email.get_emails()
    return render_template("email_success.html", email_list=email_list)

