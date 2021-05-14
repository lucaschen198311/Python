from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%M %d %Y") AS created_at FROM users;'
        users_from_db = connectToMySQL('users').query_db(query)
        return users_from_db
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id=%(id)s;"
        data = {
            "id" : id
        }
        user_from_db = connectToMySQL('users').query_db(query, data)[0]
        return user_from_db
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        user_id = connectToMySQL('users').query_db(query, data)
        return user_id
    
    @classmethod
    def delete_one(cls, id):
        query = 'DELETE FROM users WHERE id=%(id)s'
        data = {
            "id" : id
        }
        connectToMySQL('users').query_db(query, data)
    
    @classmethod
    def update_one(cls, data):
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;'
        connectToMySQL('users').query_db(query, data)
