from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors;'
        authors_from_db = connectToMySQL('books').query_db(query)
        return authors_from_db
    
    @classmethod
    def get_author(cls, data):
        query = 'SELECT * FROM authors WHERE id = %(author_id)s;'
        book = connectToMySQL('books').query_db(query, data)
        return book
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO authors (name) VALUES(%(name)s);'
        new_id = connectToMySQL('books').query_db(query, data)
        return new_id
    
    @classmethod
    def book_fav_authors(cls, data):
        query = 'SELECT * FROM books JOIN favorites ON books.id=favorites.book_id JOIN authors ON authors.id=favorites.author_id WHERE books.id=%(book_id)s;'
        book_favs = connectToMySQL('books').query_db(query, data)
        return book_favs
    
    @classmethod
    def authors_not_favs(cls, data):
        query = 'SELECT * FROM authors WHERE id NOT IN (SELECT a.id FROM authors a JOIN favorites ON favorites.author_id = a.id WHERE favorites.book_id=%(book_id)s);'
        author_list_not_fav = connectToMySQL('books').query_db(query, data)
        return author_list_not_fav
    
    @classmethod
    def add_book_fav(cls, data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES(%(author_id)s, %(book_id)s);'
        new_book_fav_id = connectToMySQL('books').query_db(query, data)
        return new_book_fav_id
    