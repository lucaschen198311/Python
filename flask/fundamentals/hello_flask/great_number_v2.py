from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = '12345@'

@app.route('/')
def index():
    if 'random_num' not in session and 'guess_num' not in session:
        session.clear()
        session['form_display'] = "form-display"
        session['guess_low_high'] = "inactive"
        session['guess_correct'] = "inactive"
        return render_template("great_number.html", form_display=session['form_display'],guess_low_high=session['guess_low_high'],guess_correct=session['guess_correct'])
    elif 'guess_num' not in session:
        session.pop('random_num')
    return render_template("great_number.html", form_display=session['form_display'],guess_low_high=session['guess_low_high'],guess_correct=session['guess_correct'], display_message=session['display_message'])

@app.route('/guess', methods=['POST'])
def guess():
    print("Got Post Info")
    print(request.form)
    # generate a random number:
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100) 
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
        session.pop('guess_num')
        
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)