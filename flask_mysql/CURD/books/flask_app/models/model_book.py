from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        books_from_db = connectToMySQL('books').query_db(query)
        return books_from_db
    
    @classmethod
    def insert_one(cls, data):
        query = 'INSERT INTO books (title, num_of_pages) VALUES(%(title)s, %(num_of_pages)s);'
        new_id = connectToMySQL('books').query_db(query, data)
        return new_id
    
    @classmethod
    def get_book_id(cls, data):
        query = 'SELECT id FROM books WHERE title = %(title)s;'
        book_id = connectToMySQL('books').query_db(query, data)
        return book_id
    
    @classmethod
    def author_fav_books(cls, data):
        query = 'SELECT * FROM authors JOIN favorites ON authors.id=favorites.author_id JOIN books ON books.id=favorites.book_id WHERE authors.id=%(author_id)s;'
        author_favs = connectToMySQL('books').query_db(query, data)
        return author_favs
    
    @classmethod
    def books_not_favs(cls, data):
        query = 'SELECT * FROM books WHERE id NOT IN (SELECT a.id FROM books a JOIN favorites ON favorites.book_id = a.id WHERE favorites.author_id=%(author_id)s);'
        book_list_not_fav = connectToMySQL('books').query_db(query, data)
        return book_list_not_fav
    
    @classmethod
    def add_author_fav(cls, data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES(%(author_id)s, %(book_id)s);'
        new_author_fav_id = connectToMySQL('books').query_db(query, data)
        return new_author_fav_id