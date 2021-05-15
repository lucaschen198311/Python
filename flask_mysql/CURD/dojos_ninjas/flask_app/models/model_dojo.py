from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_ninjas').query_db(query)
        return dojos_from_db

    @classmethod
    def get_id(cls,name):
        data={
            "name" : name
        }
        query = 'SELECT id FROM dojos WHERE name=%(name)s;'
        id = connectToMySQL('dojos_ninjas').query_db(query, data)
        return id
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO dojos (name) VALUES(%(name)s);'
        dojo_new_id = connectToMySQL('dojos_ninjas').query_db(query, data)
        return dojo_new_id
    
    