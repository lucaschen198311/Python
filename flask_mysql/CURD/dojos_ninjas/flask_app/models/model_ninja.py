from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["first_name"]
        self.name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        ninjas_from_db = connectToMySQL('dojos_ninjas').query_db(query)
        return ninjas_from_db
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        ninja_new_id = connectToMySQL('dojos_ninjas').query_db(query, data)
        return ninja_new_id
    
    @classmethod
    def ninja_dojo_join(cls,data):
        query = 'SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id=dojos.id WHERE dojos.id=%(id)s;'
        ninja_dojo_join = connectToMySQL('dojos_ninjas').query_db(query, data)
        return ninja_dojo_join