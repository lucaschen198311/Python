from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = '12345@'

@app.route('/')
def index():
    session.clear()
    session['form_display'] = "form-display"
    session['guess_low_high'] = "inactive"
    session['guess_correct'] = "inactive"
    session['counter'] = 0
    return render_template("great_number.html", form_display=session['form_display'],guess_low_high=session['guess_low_high'],guess_correct=session['guess_correct'], counter=session['counter'])

@app.route('/guess', methods=['POST'])
def guess():
    print("Got Post Info")
    print(request.form)
    # generate a random number:
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100) 
    print("Random number is :" + str(session['random_num']))
    session['guess_num'] = request.form['number']
    print("guess number is " + session['guess_num'] )
    if int(session['guess_num']) > session['random_num']:
        session['display_message'] = "Too High!"
        session['guess_low_high'] = "guess_low_high"
    elif int(session['guess_num']) < session['random_num']:
        session['display_message'] = "Too Low!"
        session['guess_low_high'] = "guess_low_high"
    else:
        session['display_message'] = session['guess_num'] + " was the number!"
        session['guess_low_high'] = "inactive"
        session['form_display'] = "inactive"
        session['guess_correct'] = "guess_correct"
    session['counter'] += 1    
    return redirect('/display')

@app.route('/display')
def display_result():
    if session['counter']<=5:
        return render_template("great_number.html", form_display=session['form_display'],guess_low_high=session['guess_low_high'],guess_correct=session['guess_correct'], display_message=session['display_message'], counter=session['counter'])
    else:
        session['display_message'] = "Exceed Limited Times and Lose!"
        session['form_display'] = "inactive"
        session['guess_low_high'] = "inactive"
        session['guess_correct'] = "guess_correct"
        return render_template("great_number.html", form_display=session['form_display'],guess_low_high=session['guess_low_high'],guess_correct=session['guess_correct'], display_message=session['display_message'], counter=session['counter'])


if __name__ == "__main__":
    app.run(debug=True)