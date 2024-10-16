import hashlib
import random
import string

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility function to validate passwords
def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()

# Utility function to generate a random visitor ID
def generate_visitor_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Utility function to allocate a random ride based on visitor's disability type
def allocate_ride_based_on_disability(disability):
    ride_options = {
        'mobility': ['Wheelchair-Friendly Coaster', 'Accessible Ferris Wheel'],
        'sensory': ['Sensory-Friendly Carousel', 'Quiet Adventure Ride'],
        'none': ['Standard Roller Coaster', 'Bumper Cars']
    }
    
    if disability in ride_options:
        return random.choice(ride_options[disability])
    return random.choice(ride_options['none'])

# Utility function to generate random sign descriptions for assistive technologies
def generate_sign_description():
    descriptions = [
        'Use this path for easier navigation.',
        'Audio assistance available here.',
        'Follow the green signs for wheelchair accessibility.',
        'Sensory-friendly zone ahead.',
    ]
    return random.choice(descriptions)

# Utility function to calculate available capacity in a rest area
def calculate_available_capacity(current_occupancy, max_capacity):
    return max(0, max_capacity - current_occupancy)
