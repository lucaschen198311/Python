from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Message:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.recipient_id = data["recipient_id"]
        self.account_id = data["account_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_message_to_account(cls, data):
        query = 'SELECT m.id, m.content,m.recipient_id,m.created_at, a.first_name, a.last_name, TIMESTAMPDIFF(MINUTE, m.created_at, NOW()) AS minute, TIMESTAMPDIFF(HOUR, m.created_at, NOW()) AS hour, TIMESTAMPDIFF(DAY, m.created_at, NOW()) AS day, TIMESTAMPDIFF(MONTH, m.created_at, NOW()) AS month FROM message m JOIN account a ON m.account_id=a.id WHERE m.recipient_id=%(id)s ORDER BY m.created_at DESC;'
        messages = connectToMySQL('private_wall').query_db(query, data)
        return messages
    
    @classmethod
    def total_message_sent(cls, data):
        query = 'SELECT COUNT(*) as total_sent FROM message WHERE account_id = %(id)s;'
        total_sent = connectToMySQL('private_wall').query_db(query, data)
        return total_sent
    
    @classmethod
    def total_message_received(cls, data):
        query = 'SELECT COUNT(*) as total_received FROM message WHERE recipient_id = %(id)s;'
        total_received = connectToMySQL('private_wall').query_db(query, data)
        return total_received
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO message (content, recipient_id, account_id) VALUES(%(content)s, %(recipient_id)s, %(account_id)s);'
        new_message_id = connectToMySQL('private_wall').query_db(query, data)
        return new_message_id
    
    @classmethod
    def delete_one(cls, data):
        query = 'DELETE FROM message WHERE id=%(message_id)s;'
        connectToMySQL('private_wall').query_db(query, data)
    
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form["content"])<5:
            flash("The message should be 5 characters at least.")
            is_valid = False
        return is_valid
    
        