from flask import Flask, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_cors import CORS  # type: ignore # Import CORS
from config import Config

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config.from_object(Config)
db = SQLAlchemy(app)

# Test Database Connectivity
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Try to query the database
        db.session.execute('SELECT 1')
        return jsonify({"message": "Database connection is successful!"}), 200
    except Exception as e:
        return jsonify({"message": "Database connection failed!", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
