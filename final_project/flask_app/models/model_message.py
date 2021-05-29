from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.content = data["content"]
        self.sent_to = data["sent_to"]
        self.account_id = data["account_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_message_received(cls, data):
        query = 'SELECT * FROM message WHERE sent_to=%(sent_to)s ORDER BY created_at DESC;'
        messages = connectToMySQL('freelancer').query_db(query, data)
        return messages
    
    @classmethod
    def get_total_message_received(cls, data):
        query = 'SELECT COUNT(*) AS total_received FROM message WHERE sent_to=%(sent_to)s;'
        total_received = connectToMySQL('freelancer').query_db(query, data)
        return total_received
    
    @classmethod
    def display_message(cls, data):
        query = 'SELECT m.id, m.title, m.content, m.sent_to, m.created_at, m.account_id, ac.username FROM message m JOIN account ac ON m.account_id = ac.id WHERE m.id=%(id)s;'
        message = connectToMySQL('freelancer').query_db(query, data)
        return message
    
    @classmethod
    def send_message(cls, data):
        query = 'INSERT INTO message (title, content, sent_to, account_id) VALUES(%(title)s, %(content)s, %(sent_to)s, %(account_id)s);'
        new_message_id = connectToMySQL('freelancer').query_db(query, data)
        return new_message_id
    
    @classmethod
    def delete_message(cls, data):
        query = 'DELETE FROM message WHERE id=%(id)s;'
        connectToMySQL('freelancer').query_db(query, data)
    
    @staticmethod
    def validate_message(form):
        is_valid = True
        if len(form["content"])< 1:
            flash("Message couldn't be empty.")
            is_valid = False
        if len(form["sent_to"])< 3:
            flash("Please input correct username.")
            is_valid = False
        if len(form["title"])< 2:
            flash("Please input correct title.")
            is_valid = False
        return is_valid
    