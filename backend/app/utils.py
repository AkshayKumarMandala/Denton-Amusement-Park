import hashlib

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility function to validate passwords
def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()
