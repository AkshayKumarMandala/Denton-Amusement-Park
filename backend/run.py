from app import app, db

if __name__ == '__main__':
    # Push application context before creating tables
    with app.app_context():
        db.create_all()  # Creates the tables based on models
    
    app.run(debug=True)
