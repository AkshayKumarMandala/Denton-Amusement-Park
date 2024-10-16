from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import api  # Import your routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update with your DB config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)  # Enable CORS for all routes

    db.init_app(app)  # Initialize your database
    app.register_blueprint(api)  # Register the API blueprint

    return app
