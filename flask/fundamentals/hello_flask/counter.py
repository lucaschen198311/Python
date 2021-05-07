from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Oldman1983@'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] = str(int(session['counter']) + 1)
    else:
        session['counter'] = "1"
    return render_template("counter.html", counter=session['counter'])

@app.route('/addtwice')
def add_twice():
    print("Add Twice Visit")
    session['counter'] = str(int(session['counter']) + 1)
    return redirect('/')

@app.route('/destroy_session')
def reset():
    print("Reset")
    session.pop('counter')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    
