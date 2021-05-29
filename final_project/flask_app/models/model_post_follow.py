from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post_Follow:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.post_purpose = data["post_purpose"]
        self.category = data["category"]
        self.description = data["description"]
        self.price = data["price"]
        self.status = data["status"]
        self.account_id = data["account_id"]
        self.address_id = data["address_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def display_post_follows(cls, data):
        query = 'SELECT pf.id, pf.content, pf.post_id, pf.account_id, pf.created_at, ac.username FROM post_follow pf JOIN post p ON p.id = pf.post_id JOIN account ac ON pf.account_id = ac.id WHERE p.id=%(id)s;'
        posts = connectToMySQL('freelancer').query_db(query, data)
        return posts
    
    @classmethod
    def posts_followed_by_user(cls, data):
        query = 'SELECT DISTINCT p.id, p.title, p.created_at FROM post_follow pf JOIN account ac ON ac.id = pf.account_id JOIN post p ON p.id = pf.post_id WHERE pf.account_id=%(account_id)s;'
        total_posts_followed = connectToMySQL('freelancer').query_db(query, data)
        return total_posts_followed
    
    @classmethod
    def get_total_follows(cls, data):
        query = 'SELECT COUNT(*) AS total_posts_followed FROM post_follow WHERE account_id=%(account_id)s;'
        total_follows = connectToMySQL('freelancer').query_db(query, data)
        return total_follows
    
    @classmethod
    def create_follow(cls, data):
        query = 'INSERT INTO post_follow (content, post_id, account_id) VALUES(%(content)s, %(post_id)s, %(account_id)s);'
        new_follow_id = connectToMySQL('freelancer').query_db(query, data)
        return new_follow_id
    
    @staticmethod
    def validate_follow(form):
        is_valid = True
        if len(form["content"])< 1:
            flash("Message couldn't be empty.")
            is_valid = False
        return is_valid
    
    
    
    