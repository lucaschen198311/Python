from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("dojo_survey.html")
    
@app.route('/result', methods=['POST'])
def create_survey():
    print("Got Post Info")
    print(request.form)
    name_form = request.form['name']
    location_form = request.form['location']
    language_form  = request.form['language']
    comment_form = request.form['comment']
    return render_template("dojo_survey_show.html", name = name_form, location = location_form, language = language_form, comment = comment_form)

if __name__ == "__main__":
    app.run(debug=True)