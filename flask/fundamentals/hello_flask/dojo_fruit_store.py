from flask import Flask, render_template, request, redirect
from datetime import datetime, date
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("dojo_fruits_index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]
    fruit_list = ["strawberry","raspberry","apple","blackberry"]
    order_list = []
    total_count = 0
    dt_string = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    for fruit in fruit_list:
        if request.form[fruit] != "0":
            order_list.append((fruit, request.form[fruit]))
            total_count += int(request.form[fruit])
    return render_template("dojo_fruits_checkout.html", first_name = first_name,last_name = last_name,student_id = student_id, order_list = order_list, total_count = total_count,dt_string=dt_string)

@app.route('/fruits')         
def fruits():
    return render_template("dojo_fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    