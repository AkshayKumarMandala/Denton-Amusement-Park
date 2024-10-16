from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for demo purposes
visitors = []
rides = []
animals = []

@app.route('/visitors', methods=['GET', 'POST'])
def visitor_handler():
    if request.method == 'POST':
        visitor = request.json
        visitors.append(visitor)
        return jsonify({'message': 'Visitor added successfully', 'visitor': visitor}), 201
    else:
        return jsonify(visitors), 200

@app.route('/admin/respond', methods=['POST'])
def admin_response():
    data = request.json
    visitor_id = data.get('visitor_id')
    response = data.get('response')
    return jsonify({'message': f'Response sent to visitor {visitor_id}', 'response': response}), 200

@app.route('/rides/allocate', methods=['POST'])
def allocate_ride():
    ride_info = request.json
    rides.append(ride_info)
    return jsonify({'message': 'Ride allocated', 'ride_info': ride_info}), 201

@app.route('/service_animal/feed', methods=['POST'])
def feed_service_animal():
    animal_info = request.json
    animals.append(animal_info)
    return jsonify({'message': 'Service animal facility used', 'animal_info': animal_info}), 201

if __name__ == '__main__':
    app.run(debug=True)
