from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Account:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.password = data["password"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_account_by_id(cls, data):
        query = 'SELECT * FROM account WHERE id=%(id)s;'
        accounts_from_db = connectToMySQL('recipe').query_db(query, data)
        accounts = []
        for a in accounts_from_db:
            accounts.append(cls(a))
        return accounts
    
    @classmethod
    def get_account_exclude_id(cls, data):
        query = 'SELECT * FROM account WHERE id <> %(id)s ORDER BY first_name;'
        account_list = connectToMySQL('recipe').query_db(query, data)
        accounts = []
        for a in account_list:
            accounts.append(cls(a))
        return accounts
    
    @classmethod
    def get_account_by_email(cls, data):
        query = 'SELECT * FROM account WHERE email=%(email)s;'
        account = connectToMySQL('recipe').query_db(query, data)
        #accounts = []
        #for a in account:
            #accounts.append(cls(a))
        return account
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO account (first_name, last_name,email,password) VALUES(%(first_name)s, %(last_name)s, %(email)s,%(password)s);'
        new_account_id = connectToMySQL('recipe').query_db(query, data)
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
        if not EMAIL_REGEX.match(form["email"]):
            flash("Email format is incorrect!",'email')
            is_valid = False
        if len(form["password"])<8:
            flash("Password is too short and must be 8 length at least.",'password')
            is_valid = False
        if form["password"] != form["confirm_password"]:
            flash("Password must be equal!",'password')
            is_valid = False
        return is_valid
    