from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_recipe import Recipe
    
@app.route('/recipes/new')
def new_recipe():
    return render_template("form.html")

@app.route('/recipes/create', methods=["POST"])
def create_new_recipe():
    print(request.form)
    is_valid = Recipe.validate_form(request.form)
    if not is_valid:
        return redirect('/recipes/new')
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "under_thirtymin" : request.form["under_thirtymin"],
        "account_id" : session["user_id"]
    }
    print(data)
    Recipe.insert_one(data)
    return redirect('/recipes')

@app.route('/recipes/<recipe_id>/edit')
def show_edit_recipe(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    session["recipe_id"] = recipe_id
    recipe = Recipe.get_recipe_by_id(data)
    print(recipe[0].id)
    return render_template("edit_recipe.html", recipe=recipe)

@app.route('/recipes/update', methods=["POST"])
def update_recipe():
    is_valid = Recipe.validate_form(request.form)
    if not is_valid:
        return redirect(f"/recipes/{session['recipe_id']}/edit")
    data = {
        "id" : session["recipe_id"],
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "under_thirtymin" : request.form["under_thirtymin"]
    }
    Recipe.update_one(data)
    return redirect('/recipes')

@app.route('/recipes/<recipe_id>/delete')
def delete_recipe(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    Recipe.delete_one(data)
    return redirect('/recipes')

@app.route('/recipes/<recipe_id>')
def show_recipe(recipe_id):
    data = {
        "recipe_id" : recipe_id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template("show_recipe.html", recipe=recipe)