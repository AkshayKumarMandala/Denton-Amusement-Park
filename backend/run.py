from app import app, db
from flask_cors import CORS

# Enable CORS for all routes
CORS(app)

if __name__ == '__main__':
    # Push application context before creating tables
    with app.app_context():
        db.create_all()  # Creates the tables based on models
    
    app.run(debug=True)

