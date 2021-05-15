from flask_app import app
from flask_app.controllers import controller_authors
from flask_app.controllers import controller_books

if __name__ == "__main__":
    app.run(debug=True)