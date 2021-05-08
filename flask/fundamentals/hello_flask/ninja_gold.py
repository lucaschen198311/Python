from flask import Flask, render_template, request, redirect, session
from datetime import datetime, date
import random

app = Flask(__name__)
app.secret_key = 'Oldman1983@'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['log_list'] = []
    return render_template("ninja_gold.html" , total_gold=session['total_gold'], log_list=session['log_list'])

@app.route('/process_money', methods=["POST"])
def process_money():
    print("Got Post Info")
    print(request.form)
    
    time_point = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    if request.form['building'] == "reset":
        session.clear()
    else:
        if request.form['building'] == "farm":
            session['earn'] = random.randint(10, 20)
            log = f"Earned {session['earn']} golds from the farm! ({time_point})"
        elif request.form['building'] == "cave":
            session['earn'] = random.randint(5, 10)
            log = f"Earned {session['earn']} golds from the cave! ({time_point})"
        elif request.form['building'] == "house":
            session['earn'] = random.randint(2, 5)
            log = f"Earned {session['earn']} golds from the house! ({time_point})"
        else:
            session['earn'] = random.randint(-50, 50)
            if session['earn']>=0:
                log = f"Enter a casino and earn {session['earn']} golds! ({time_point})"
            else:
                log = f"Enter a casino and lost {session['earn']} golds! ({time_point})"
    
        if session['earn']>=0:
            session['log_list'].append(("+", log))
        else:
            session['log_list'].append(("-", log))
        session['total_gold'] += session['earn']

    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)