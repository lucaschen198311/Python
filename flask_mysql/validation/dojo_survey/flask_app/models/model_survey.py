from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Survey:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_survey(cls, data):
        query = 'SELECT * FROM dojo_survey WHERE name=%(name)s;'
        user_from_db = connectToMySQL('dojo_survey').query_db(query, data)
        return user_from_db
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO dojo_survey (name, location, language, comment) VALUES(%(name)s, %(location)s, %(language)s, %(comment)s);'
        survey_new_id = connectToMySQL('dojo_survey').query_db(query, data)
        return survey_new_id

    @staticmethod
    def validate_form(form):
        is_valid = True
        if not form["name"].replace(" ","").isalpha():
            flash("Name must be characters. Please input correct name.")
            is_valid = False
        if len(form["comment"])>200:
            flash("Input is too much. Please use less than 200 characters.")
            is_valid = False
        return is_valid
    