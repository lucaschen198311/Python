from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_account import Account
from flask_app.models.model_post import Post
from flask_app.models.model_post_follow import Post_Follow
from flask_app.models.model_message import Message

@app.route('/')
def index():
    if "user_id" in session:
        return redirect("/dashboard")
    else:
        data = {}
        category_list = ["education", "living", "traveling", "friends", "sports", "tech"]
        for category in category_list:
            data1 = {
                "category" : category
            }
            data[category + "_posts"] = Post.get_most_recent_posts_by_category(data1)
        return render_template("home.html", data=data)

@app.route('/dashboard')
def login_successs():
    if "user_id" not in session:
        return redirect("/")
    else:
        data = {
            "account_id" : session["user_id"],
            "sent_to" : session["username"]
        }
        my_posts = Post.get_posts_own(data)
        total_posts = Post.get_total_posts_own(data)
        my_follows = Post_Follow.posts_followed_by_user(data)
        messages = Message.get_message_received(data)
        total_message = Message.get_total_message_received(data)
        recent_posts = Post.most_recent_posts()
        return render_template("user_home.html", username=session["username"], my_posts=my_posts, total_posts=total_posts, my_follows=my_follows, messages=messages, total_message=total_message, recent_posts =recent_posts)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')