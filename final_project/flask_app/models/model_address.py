from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Address:
    def __init__(self, data):
        self.id = data["id"]
        self.street = data["street"]
        self.city = data["city"]
        self.state = data["state"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_adress_by_id(cls, data):
        query = 'SELECT * FROM adress WHERE id=%(id)s;'
        adress = connectToMySQL('freelancer').query_db(query, data)
        return adress
    
    @classmethod
    def insert_address(cls, data):
        query = 'INSERT INTO address (street, city, state) VALUES (%(street)s, %(city)s, %(state)s);'
        new_address_id = connectToMySQL('freelancer').query_db(query, data)
        return new_address_id
    
    @staticmethod
    def validate_address(form):
        is_valid = True
        if len(form["city"])< 3:
            flash("Please enter correct city name.")
            is_valid = False
        if len(form["state"])!=2:
            flash("Please use 2 letter abbreviation for US state.")
            is_valid = False
        return is_valid
    