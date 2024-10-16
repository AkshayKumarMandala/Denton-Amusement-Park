from flask import Flask
from app.routes import setup_routes
from app.utils import initialize_db

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('../config.py')

    # Initialize the database
    initialize_db(app)

    # Register routes
    setup_routes(app)

    return app

