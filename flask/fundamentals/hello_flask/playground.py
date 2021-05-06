from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/play')
def playground_1():
    return render_template("playground_1.html")

@app.route('/play/<times>')
def playground_2(times):
    return render_template("playground_2.html", replicate = int(times))

@app.route('/play/<times>/<color>')
def playground_3(times, color):
    return render_template("playground_3.html", replicate = int(times), background = color)

@app.errorhandler(Exception)
def server_error(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)
    
