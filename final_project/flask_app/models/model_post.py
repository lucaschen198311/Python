from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
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
    def get_post_by_id(cls, data):
        query = 'SELECT * FROM post WHERE id=%(id)s;'
        post = connectToMySQL('freelancer').query_db(query, data)
        return post
    
    @classmethod
    def get_posts_own(cls, data):
        query = 'SELECT * FROM post WHERE account_id=%(account_id)s ORDER BY created_at DESC;'
        posts = connectToMySQL('freelancer').query_db(query, data)
        return posts
    
    @classmethod
    def get_total_posts_own(cls, data):
        query = 'SELECT COUNT(*) AS total_posts FROM post WHERE account_id=%(account_id)s;'
        total_posts = connectToMySQL('freelancer').query_db(query, data)
        return total_posts
    
    @classmethod
    def most_recent_posts(cls):
        query = 'SELECT p.id, p.title, p.post_purpose, p.category, p.account_id, ac.username, ad.city, ad.state FROM post p JOIN account ac ON p.account_id = ac.id JOIN address ad ON p.address_id = ad.id ORDER BY p.created_at DESC LIMIT 10;'
        posts = connectToMySQL('freelancer').query_db(query)
        return posts
    
    @classmethod
    def get_most_recent_posts_by_category(cls, data):
        query = 'SELECT * FROM post WHERE category = %(category)s ORDER BY created_at DESC LIMIT 10;'
        posts = connectToMySQL('freelancer').query_db(query, data)
        return posts
    
    """
    This is for search posts based on several condiditons which can be followed up 
    after MERN applied.
    
    @classmethod
    def search_posts(cls, data):
        if data == {}:
            query = 'SELECT p.id, p.title, p.post_purpose, p.category,p.created_at, p.account_id, p.address_id, ac.username, ad.city, ad.state, TIMESTAMPDIFF(DAY, p.created_at, NOW()) as time_diff FROM post p JOIN account ac ON p.account_id=ac.id JOIN address ad ON p.address_id=ad.id ORDER BY p.created_at LIMIT 10;'
        else:
            query = 'SELECT p.id, p.title, p.post_purpose, p.category,p.created_at, p.account_id, p.address_id, ac.username, ad.city, ad.state, TIMESTAMPDIFF(DAY, p.created_at, NOW()) as time_diff FROM post p JOIN account ac ON p.account_id=ac.id JOIN address ad ON p.address_id=ad.id WHERE %(conditions)s ORDER BY p.created_at LIMIT 10;' 
        search_posts = connectToMySQL('freelancer').query_db(query, data)
        return search_posts
        
    """
        
    @classmethod
    def display_post(cls, data):
        query = 'SELECT p.id, p.title, p.post_purpose, p.category, p.description, p.price, p.status, p.created_at, p.account_id, ac.username, ad.city, ad.state FROM post p JOIN account ac ON p.account_id = ac.id JOIN address ad ON p.address_id = ad.id WHERE p.id=%(id)s;'
        post = connectToMySQL('freelancer').query_db(query, data)
        return post
    
    @classmethod
    def create_post(cls, data):
        query = 'INSERT INTO post (title, post_purpose, category, description, price, account_id, address_id) VALUES(%(title)s, %(post_purpose)s, %(category)s, %(description)s, %(price)s, %(account_id)s, %(address_id)s);'
        new_post_id = connectToMySQL('freelancer').query_db(query, data)
        return new_post_id
    
    @staticmethod
    def validate_post(form):
        is_valid = True
        if len(form["title"])< 2:
            flash("Please enter correct title.")
            is_valid = False
        if len(form["description"])<2:
            flash("Description can't be empty.")
            is_valid = False
        return is_valid
    
    
    
    