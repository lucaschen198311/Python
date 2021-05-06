from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_Dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    return "Hi " + name + "!"

@app.route('/repeat/<times>/<word>')
def word_repeat(times,word):
    return (word + " ") *int(times)

@app.errorhandler(Exception)
def server_error(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)