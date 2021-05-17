from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_emails(cls):
        query = 'SELECT * FROM email;'
        email_list = connectToMySQL('email').query_db(query)
        return email_list
    
    @classmethod
    def validate_email(cls, data):
        query = 'SELECT * FROM email WHERE email=%(email)s;'
        email_exist = connectToMySQL('email').query_db(query, data)
        return email_exist
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO email (email) VALUES(%(email)s);'
        email_new_id = connectToMySQL('email').query_db(query, data)
        return email_new_id

    @staticmethod
    def validate_form(email_exist, data):
        is_valid = True
        if len(data["email"]) == 0:
            flash("Please enter valid email address. It can't be void!", 'email')
            is_valid = False
        if len(email_exist)>0:
            flash("Email already exists!" 'email')
            is_valid = False
        return is_valid
    