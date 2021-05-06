from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkboard_1():
    return render_template("checkboard.html", row = 8, col = 8)
    
@app.route('/<n>')
def checkboard_2(n):
    return render_template("checkboard.html", row = int(n), col = int(n))

@app.route('/<n>/<m>')
def checkboard_3(n, m):
    return render_template("checkboard.html", row = int(n), col = int(m))

@app.route('/<n>/<m>/<color1>/<color2>')
def checkboard_4(n, m, color1, color2):
    return render_template("checkboard.html", row = int(n), col = int(m), color_1 = color1, color_2 = color2)

@app.errorhandler(Exception)
def server_error(err):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)