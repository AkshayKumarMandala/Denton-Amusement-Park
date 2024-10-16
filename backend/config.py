import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    # Database connection URL: Modify according to your DB setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:Pass@localhost/denton_amusement'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Additional configurations
    CORS_HEADERS = 'Content-Type'  # Support for CORS headers
    JSONIFY_PRETTYPRINT_REGULAR = True  # Enable pretty print for JSON responses

    # Config for session handling (Optional)
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
