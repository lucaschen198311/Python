from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book

@app.route("/authors")
def authors():
    author_list = Author.get_all()
    print(author_list)
    return render_template("authors.html", author_list = author_list)

@app.route("/authors/add", methods=["POST"])
def add_author():
    data = {
        "name": request.form["name"]
    }
    Author.insert_one(data)
    return redirect('/authors')


@app.route("/authors/<author_id>")
def show_author_fav(author_id):
    session["author_id"] = author_id
    data = {
        "author_id" : author_id
    }
    author_favs = Book.author_fav_books(data)
    print(author_favs)
    book_list_not_fav = Book.books_not_favs(data)
    print(book_list_not_fav)
    return render_template("author_show.html", author_favs=author_favs, book_list_not_fav=book_list_not_fav)

@app.route("/authors/add_author_fav", methods=["POST"])
def add_author_favebook():
    data = {
        "author_id" : session["author_id"],
        "book_id" : request.form["book_select"]
    }
    Book.add_author_fav(data)
    return redirect(f"/authors/{session['author_id']}")
    #return redirect("/authors")
