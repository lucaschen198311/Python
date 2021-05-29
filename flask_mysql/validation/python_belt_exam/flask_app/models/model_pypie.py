from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Pypie:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.filling = data["filling"]
        self.crust = data["crust"]
        self.vote = data["vote"]
        self.account_id = data["account_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all_pies(cls):
        query = 'SELECT p.id, p.name, p.vote,a.first_name, a.last_name FROM pypie p JOIN account a ON p.account_id=a.id ORDER BY p.vote DESC;'
        all_pypies = connectToMySQL('pypie').query_db(query)
        #pypies = []
        #for p in all_pypies:
            #pypies.append(cls(p))
        return all_pypies
                
    @classmethod
    def get_pypie_by_account(cls, data):
        query = 'SELECT * FROM pypie WHERE account_id=%(id)s;'
        pypies_from_db = connectToMySQL('pypie').query_db(query, data)
        pypies = []
        for p in pypies_from_db:
            pypies.append(cls(p))
        return pypies
    
    @classmethod
    def get_pypie_by_id(cls, data):
        query = 'SELECT * FROM pypie WHERE id=%(pypie_id)s;'
        pypie_from_db = connectToMySQL('pypie').query_db(query, data)
        pypie = []
        for p in pypie_from_db:
            pypie.append(cls(p))
        return pypie 
    
    @classmethod
    def get_account_name_by_pypieid(cls,data):
        query='SELECT first_name, last_name FROM account JOIN pypie on account.id=pypie.account_id WHERE pypie.id=%(pypie_id)s;'
        name = connectToMySQL('pypie').query_db(query, data)
        return name
        
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO pypie (name, filling, crust, account_id) VALUES(%(name)s, %(filling)s, %(crust)s, %(account_id)s);'
        new_pypie_id = connectToMySQL('pypie').query_db(query, data)
        return new_pypie_id
    
    @classmethod
    def update_one(cls, data):
        query = 'UPDATE pypie SET name=%(name)s, filling=%(filling)s, crust=%(crust)s WHERE id=%(id)s;'
        connectToMySQL('pypie').query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        query = 'DELETE FROM pypie WHERE id=%(pypie_id)s;'
        connectToMySQL('pypie').query_db(query, data)
    
    @classmethod
    def vote(cls, data):
        query='UPDATE pypie SET vote=vote+1 WHERE id=%(pypie_id)s'
        connectToMySQL('pypie').query_db(query, data)
    
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form["name"])<1:
            flash("Name must be filled out.")
            is_valid = False
        if len(form["filling"])<1:
            flash("filling must be filled out.")
            is_valid = False
        if len(form["crust"])<1:
            flash("Crust must be filled out.")
            is_valid = False
        return is_valid
    
        