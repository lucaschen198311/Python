from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_survey import Survey

@app.route('/')
def index():
    return render_template("dojo_survey.html")
    
@app.route('/result', methods=['POST'])
def create_survey():
    print("Got Post Info")
    print(request.form)
    data ={
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    
    if not Survey.validate_form(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Survey.insert_one(data)
    #user = Survey.get_survey(data)
    #print(user)
    return render_template("dojo_survey_show.html", data=data)

