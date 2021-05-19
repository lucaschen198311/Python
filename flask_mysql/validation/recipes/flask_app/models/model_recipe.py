from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.under_30min = data["under_30min"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_recipe_by_account(cls, data):
        query = 'SELECT * FROM recipe WHERE account_id=%(id)s;'
        recipes_from_db = connectToMySQL('recipe').query_db(query, data)
        recipes = []
        for r in recipes_from_db:
            recipes.append(cls(r))
        return recipes
    
    @classmethod
    def get_recipe_by_id(cls, data):
        query = 'SELECT * FROM recipe WHERE id=%(recipe_id)s;'
        recipe_from_db = connectToMySQL('recipe').query_db(query, data)
        recipe = []
        for r in recipe_from_db:
            recipe.append(cls(r))
        return recipe
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO recipe (name, description, instruction, under_30min, account_id) VALUES(%(name)s, %(description)s, %(instruction)s, %(under_thirtymin)s, %(account_id)s);'
        new_recipe_id = connectToMySQL('recipe').query_db(query, data)
        return new_recipe_id
    
    @classmethod
    def update_one(cls, data):
        query = 'UPDATE recipe SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, under_30min=%(under_thirtymin)s WHERE id=%(id)s;'
        connectToMySQL('recipe').query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        query = 'DELETE FROM recipe WHERE id=%(recipe_id)s;'
        connectToMySQL('recipe').query_db(query, data)
    
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form["description"])<5:
            flash("The description should be 5 characters at least.")
            is_valid = False
        if len(form["instruction"])<5:
            flash("The instruction should be 5 characters at least.")
            is_valid = False
        if form["under_thirtymin"] not in ["Yes", "No"]:
            flash("Please choose the option in radio box.")
            is_valid = False
        return is_valid
    
        