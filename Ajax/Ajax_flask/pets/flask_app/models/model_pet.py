from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pet:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.vote = data["vote"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM pets;'
        pet_list = connectToMySQL('pets').query_db(query)
        return pet_list
    
    @classmethod
    def get_pet_by_id(cls, data):
        query = 'SELECT * FROM pets WHERE id=%(id)s;'
        pet = connectToMySQL('pets').query_db(query, data)
        return pet
        
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO pets (name, type) VALUES(%(name)s, %(type)s);'
        new_pet_id = connectToMySQL('pets').query_db(query, data)
        return new_pet_id
    
    @classmethod
    def delete_one(cls, data):
        query = 'DELETE FROM pets WHERE id=%(id)s;'
        connectToMySQL('pets').query_db(query, data)
    
    @classmethod
    def vote_up(cls, data):
        query= 'UPDATE pets SET vote = vote + 1 WHERE id=%(id)s;'
        connectToMySQL('pets').query_db(query, data)
    
    @classmethod
    def vote_down(cls, data):
        query= 'UPDATE pets SET vote = vote - 1 WHERE id=%(id)s AND vote>0;'
        connectToMySQL('pets').query_db(query, data)
    
    @classmethod
    def get_vote_by_id(cls, data):
        query='SELECT vote FROM pets WHERE id=%(id)s;'
        vote = connectToMySQL('pets').query_db(query, data)
        return vote

    @staticmethod
    def validate_add(form):
        is_valid = True
        if len(form["name"])< 1:
            flash("Name is required.")
            is_valid = False
        if len(form["type"])<1:
            flash("Type is required.")
            is_valid = False
        return is_valid
    