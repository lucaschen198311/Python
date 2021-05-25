from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_pet import Pet

@app.route('/')
def index():
    pet_list = Pet.get_all()
    return render_template("pets.html", pet_list=pet_list)

@app.route('/add', methods=["POST"])
def add_pet():
    print(request.form)
    is_valid = Pet.validate_add(request.form)
    if not is_valid:
        return render_template("warning.html")
    data = {
        "name" : request.form["name"],
        "type" : request.form["type"]
    }
    new_pet_id = Pet.insert_one(data)
    data["id"] = new_pet_id
    pet_item = Pet.get_pet_by_id(data)
    print(pet_item)
    return render_template("add_pets.html", pet_item=pet_item)

@app.route('/delete/<pet_id>')
def delete_pet(pet_id):
    data={
        "id" : pet_id
    }
    Pet.delete_one(data)
    return "1"
    
@app.route('/upvote/<pet_id>')
def vote_up(pet_id):
    data={
        "id" : pet_id
    }
    Pet.vote_up(data)
    vote = str(Pet.get_vote_by_id(data)[0]["vote"])
    print(vote)
    return vote


@app.route('/downvote/<pet_id>')
def vote_down(pet_id):
    data={
        "id" : pet_id
    }
    Pet.vote_down(data)
    vote = str(Pet.get_vote_by_id(data)[0]["vote"])
    print(vote)
    return vote