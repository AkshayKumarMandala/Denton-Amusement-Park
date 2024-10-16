from flask import request, jsonify
from app import app, db
from app.models import User, Service, Feedback, Visitor, Ride, RestArea, AssistiveTechnology, Transportation, ServiceAnimalFacility

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


# Route to add a visitor
@app.route('/api/visitors', methods=['POST'])
def add_visitor():
    data = request.get_json()
    visitor = Visitor(name=data['name'], disability=data.get('disability'))
    db.session.add(visitor)
    db.session.commit()
    return jsonify({'message': 'Visitor added successfully', 'visitor': {'id': visitor.id, 'name': visitor.name}}), 201

# Route to get all visitors
@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    visitors = Visitor.query.all()
    result = [{'id': visitor.id, 'name': visitor.name, 'disability': visitor.disability} for visitor in visitors]
    return jsonify(result)

# Route to allocate a ride to a visitor
@app.route('/api/rides/allocate', methods=['POST'])
def allocate_ride():
    data = request.get_json()
    ride = Ride(visitor_id=data['visitor_id'], ride_type=data['ride_type'])
    db.session.add(ride)
    db.session.commit()
    return jsonify({'message': 'Ride allocated successfully', 'ride': {'visitor_id': ride.visitor_id, 'ride_type': ride.ride_type}}), 201

# Route to add a rest area
@app.route('/api/restareas', methods=['POST'])
def add_rest_area():
    data = request.get_json()
    rest_area = RestArea(description=data['description'], capacity=data['capacity'])
    db.session.add(rest_area)
    db.session.commit()
    return jsonify({'message': 'Rest area added successfully', 'rest_area': {'id': rest_area.id, 'capacity': rest_area.capacity}}), 201

# Route to get all rest areas
@app.route('/api/restareas', methods=['GET'])
def get_rest_areas():
    rest_areas = RestArea.query.all()
    result = [{'id': rest_area.id, 'description': rest_area.description, 'capacity': rest_area.capacity} for rest_area in rest_areas]
    return jsonify(result)

# Route to add assistive technology
@app.route('/api/assistive_technologies', methods=['POST'])
def add_assistive_technology():
    data = request.get_json()
    assistive_tech = AssistiveTechnology(sign_description=data['sign_description'], technology_name=data['technology_name'])
    db.session.add(assistive_tech)
    db.session.commit()
    return jsonify({'message': 'Assistive technology added successfully', 'assistive_tech': {'id': assistive_tech.id}}), 201

# Route to get all assistive technologies
@app.route('/api/assistive_technologies', methods=['GET'])
def get_assistive_technologies():
    assistive_technologies = AssistiveTechnology.query.all()
    result = [{'id': assistive_tech.id, 'sign_description': assistive_tech.sign_description, 'technology_name': assistive_tech.technology_name} for assistive_tech in assistive_technologies]
    return jsonify(result)

# Route to arrange transportation for a visitor
@app.route('/api/transportation/arrange', methods=['POST'])
def arrange_transportation():
    data = request.get_json()
    transportation = Transportation(visitor_id=data['visitor_id'], vehicle_type=data['vehicle_type'], accommodation=data['accommodation'])
    db.session.add(transportation)
    db.session.commit()
    return jsonify({'message': 'Transportation arranged successfully', 'transportation': {'visitor_id': transportation.visitor_id}}), 201

# Route to add service animal facility
@app.route('/api/service_animal_facilities', methods=['POST'])
def add_service_animal_facility():
    data = request.get_json()
    facility = ServiceAnimalFacility(facility_name=data['facility_name'], capacity=data['capacity'], description=data.get('description'))
    db.session.add(facility)
    db.session.commit()
    return jsonify({'message': 'Service animal facility added successfully', 'facility': {'id': facility.id}}), 201

# Route to get all service animal facilities
@app.route('/api/service_animal_facilities', methods=['GET'])
def get_service_animal_facilities():
    facilities = ServiceAnimalFacility.query.all()
    result = [{'id': facility.id, 'facility_name': facility.facility_name, 'capacity': facility.capacity, 'description': facility.description} for facility in facilities]
    return jsonify(result)
