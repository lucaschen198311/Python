from flask_app import app
from flask_app.controllers import controller_account
from flask_app.controllers import controller_message
from flask_app.controllers import controller_routes
from flask_app.controllers import controller_post

if __name__ == "__main__":
    app.run(debug=True)