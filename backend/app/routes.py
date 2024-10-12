from flask import request, jsonify
from app import app, db
from app.models import User, Service, Feedback

# Temporary route to add initial data to the services table
@app.route('/api/add_initial_services', methods=['GET'])
def add_initial_services():
    services = [
        {'name': 'Wheelchair-Friendly Pathways', 'description': 'Accessible paths throughout the park for wheelchair users.'},
        {'name': 'Sensory-Friendly Zones', 'description': 'Quiet and comfortable areas for visitors with sensory sensitivities.'},
        {'name': 'Inclusive Rides', 'description': 'Fun rides that accommodate visitors with different abilities.'},
        {'name': 'Assistive Technologies', 'description': 'Technology support such as audio assistance and visual guides.'}
    ]
    
    for service_data in services:
        service = Service(name=service_data['name'], description=service_data['description'])
        db.session.add(service)

    db.session.commit()
    
    return jsonify({'message': 'Initial services added successfully!'}), 201

# Route for getting all services
@app.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    if not services:
        print("No services found in the database.")
    else:
        for service in services:
            print(f"Service found: {service.name}, {service.description}")
    
    result = [{'id': service.id, 'name': service.name, 'description': service.description} for service in services]
    return jsonify(result)

# Route for adding feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')

    feedback = Feedback(user_id=user_id, message=message)
    db.session.add(feedback)
    db.session.commit()

    return jsonify({'message': 'Feedback submitted successfully'}), 201

# Route for registering a new user
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Route for logging in
@app.route('/api/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
