from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Account:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_account_by_email(cls, data):
        query = 'SELECT * FROM account WHERE email=%(email)s;'
        account = connectToMySQL('freelancer').query_db(query, data)
        return account
    
    @classmethod
    def get_account_by_username(cls, data):
        query = 'SELECT * FROM account WHERE username=%(username)s;'
        account = connectToMySQL('freelancer').query_db(query, data)
        return account
    
    @classmethod
    def get_username_by_id(cls, data):
        query = 'SELECT username FROM account WHERE id=%(id)s;'
        account = connectToMySQL('freelancer').query_db(query, data)
        return account
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO account (first_name, last_name, username, email, password) VALUES(%(first_name)s, %(last_name)s, %(username)s, %(email)s,%(password)s);'
        new_account_id = connectToMySQL('freelancer').query_db(query, data)
        return new_account_id

    @staticmethod
    def validate_regist(form):
        is_valid = True
        if len(form["first_name"])< 2:
            flash("Please enter correct first name.", 'name')
            is_valid = False
        if len(form["last_name"])<2:
            flash("Please enter correct last name.",'name')
            is_valid = False
        if len(form["username"])<3 or len(form["username"])>30:
            flash("Please enter correct username.",'name')
            is_valid = False
        if not EMAIL_REGEX.match(form["email"]):
            flash("Email format is incorrect!",'email')
            is_valid = False
        if len(form["password"])<6:
            flash("Password is too short and must be 6 length at least.",'password')
            is_valid = False
        if form["password"] != form["confirm_password"]:
            flash("Password must be equal!",'password')
            is_valid = False
        return is_valid
    