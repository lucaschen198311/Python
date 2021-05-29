from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_post import Post
from flask_app.models.model_address import Address
from flask_app.models.model_post_follow import Post_Follow

@app.route('/create_post')
def create_new_post():
    if "user_id" not in session:
        flash("please login or join us!")
        return redirect('/')
    else:
        return render_template("new_post.html")

@app.route('/post_validate', methods=["POST"])
def post_validate():
    print(request.form)
    data1 = {
        "post_purpose" : request.form["purpose"],
        "category" : request.form["category"],
        "price" : request.form["price"],
        "title" : request.form["title"],
        "description" : request.form["description"],
        "account_id" : session["user_id"]
    }
    data2 = {
        "street"  : request.form["street"],
        "city" : request.form["city"],
        "state" : request.form["state"]
    }
    if not Post.validate_post(data1) or not Address.validate_address(data2):
        return redirect("/create_post")
    new_address_id =Address.insert_address(data2)
    print(new_address_id)
    print(data2)
    data1["address_id"] = new_address_id
    new_post_id = Post.create_post(data1)
    print(new_post_id)
    print(data2)
    return redirect("/dashboard")

@app.route('/post/<post_id>')
def display_post(post_id):
    data = {
        "id" : post_id,
        #"account_id" : session["user_id"]
    }
    post = Post.display_post(data)
    data["account_id"] = post[0]["account_id"]
    total_follows = Post_Follow.get_total_follows(data)
    post_follows = Post_Follow.display_post_follows(data)
    return render_template("display_post.html",post=post, total_follows=total_follows, post_follows=post_follows)

@app.route('/post/<post_id>/go_back')
def post_goBack(post_id):
    if "user_id" not in session:
        return redirect("/")
    else:
        return redirect("/dashboard")

@app.route('/post/<post_id>/follow')
def post_reply(post_id):
    if "user_id" not in session:
        flash("Please go back to login or register!")
        return redirect(f"/post/{post_id}")
    else:
        data = {
            "id" : post_id
        }
        post = Post.get_post_by_id(data)
        return render_template("post_follow.html", post=post)

@app.route('/post/<post_id>/follow_validate', methods=["POST"])
def post_follow_validate(post_id):
    data = {
        "content" : request.form["post_follwing"], 
        "post_id" : post_id,
        "account_id" : session["user_id"]
    }
    if not Post_Follow.validate_follow(data):
        return redirect(f"/post/{post_id}/follow")
    else:
        new_follow_id = Post_Follow.create_follow(data)
        return redirect(f"/post/{post_id}")

"""
This is for search posts based on several condiditons which can be followed up 
after MERN applied.

@app.route('/search_posts', methods=["POST"])
def search_posts():
    data = {
        "purpose" : request.form["purpose"],
        "category" : request.form["category"],
        "city" : request.form["city"],
        "state" : request.form["state"],
        "time_range" : request.form["time_range"]
    }
    where_conditions = []
    if data["purpose"] != "all":
        where_conditions.append(f"p.post_purpose = {data['purpose']}") 
    if data["category"] != "all":
        where_conditions.append(f"p.category = {data['category']}")
    if data["city"] !="":
        where_conditions.append(f"ad.city = {data['city']}")
    if data["state"] !="":
        where_conditions.append(f"ad.state = {data['state']}")
    if data["time_range"] !="all":
        if data["time_range"] == "one-day":
            where_conditions.append(f"time_diff <=1")
        elif data["time_range"] == "one-week":
            where_conditions.append(f"time_diff <=7")
        elif data["time_range"] == "one-month":
            where_conditions.append(f"time_diff <=30")
        elif data["time_range"] == "beyond-one-month":
            where_conditions.append(f"time_diff >30")
    print(where_conditions)
    data1 = {}
    if len(where_conditions)>0:
        condition_str = " AND ".join(where_conditions)
        data1["conditions"] = condition_str

    recent_posts = Post.search_posts(data1)
"""