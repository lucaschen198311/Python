from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_book import Book
from flask_app.models.model_author import Author

@app.route("/books")
def books():
    book_list = Book.get_all()
    print(book_list)
    return render_template("books.html", book_list = book_list)

@app.route("/books/add", methods=["POST"])
def add_book():
    data = {
        "title" : request.form["title"],
        "num_of_pages" : request.form["num_of_pages"]
    }
    Book.insert_one(data)
    return redirect('/books')


@app.route("/books/<book_id>")
def show_book_fav(book_id):
    session["book_id"] = book_id
    data = {
        "book_id" : book_id
    }
    book_favs = Author.book_fav_authors(data)
    print(book_favs)
    author_list_not_fav = Author.authors_not_favs(data)
    print(author_list_not_fav)
    return render_template("book_show.html", book_favs=book_favs, author_list_not_fav=author_list_not_fav)

@app.route("/books/add_book_fav", methods=["POST"])
def add_book_favauthor():
    data = {
        "author_id" : request.form["author_select"],
        "book_id" : session["book_id"]
    }
    Author.add_book_fav(data)
    return redirect(f"/books/{session['book_id']}")
    #return redirect("/authors")