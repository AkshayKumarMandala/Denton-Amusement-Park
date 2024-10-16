from flask import Flask, jsonify, request
from app.models import Service, Ticket, db

app = Flask(__name__)

# Service to fetch all services
@app.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    services_data = [{'id': service.id, 'name': service.name, 'description': service.description} for service in services]
    return jsonify(services_data)

# Service to fetch all services
@app.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    # Convert the Service objects to a dictionary
    services_data = [{'id': service.id, 'name': service.name, 'description': service.description} for service in services]
    return jsonify(services_data)
# Service to add a new service
# @app.route('/api/services', methods=['POST'])
# def add_new_service():
#     data = request.get_json()
#     name = data.get('name')
#     description = data.get('description')
#     new_service = Service(name=name, description=description)
#     db.session.add(new_service)
#     db.session.commit()
#     return jsonify({'id': new_service.id, 'name': new_service.name, 'description': new_service.description}), 201

# Service to fetch tickets
@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    tickets_data = [{'id': ticket.id, 'user_id': ticket.user_id, 'service_id': ticket.service_id,
                     'ticket_type': ticket.ticket_type, 'price': str(ticket.price), 'purchase_date': ticket.purchase_date}
                    for ticket in tickets]
    return jsonify(tickets_data)

# Service to create a new ticket
@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    user_id = data.get('user_id')
    service_id = data.get('service_id')
    ticket_type = data.get('ticket_type')
    price = data.get('price')
    
    new_ticket = Ticket(user_id=user_id, service_id=service_id, ticket_type=ticket_type, price=price)
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({'id': new_ticket.id, 'user_id': new_ticket.user_id, 'service_id': new_ticket.service_id,
                    'ticket_type': new_ticket.ticket_type, 'price': str(new_ticket.price)}), 201
