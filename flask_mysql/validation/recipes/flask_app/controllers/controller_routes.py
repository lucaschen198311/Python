from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_recipe import Recipe

@app.route('/')
def index():
    if "user_id" in session:
        return redirect("/recipes")
    else:
        return render_template("regist_login.html")

@app.route('/recipes')
def login_successs():
    if "user_id" not in session:
        return redirect("/")
    else:
        data = {
            "id" : session["user_id"]
        }
        recipes = Recipe.get_recipe_by_account(data)
        print(recipes)
        return render_template("recipes.html", recipes=recipes, first_name=session["first_name"])
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')