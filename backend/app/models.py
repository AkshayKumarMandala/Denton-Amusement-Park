from app import db

# User model (unchanged)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Service model (unchanged)
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

# Feedback model (unchanged)
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    disability = db.Column(db.String(100), nullable=True)
    rides = db.relationship('Ride', backref='visitor', lazy=True)

# Ride model
class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'), nullable=False)
    ride_type = db.Column(db.String(100), nullable=False)

# Rest Area model
class RestArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    capacity = db.Column(db.Integer, nullable=False)

# Assistive Technology model
class AssistiveTechnology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sign_description = db.Column(db.Text)
    technology_name = db.Column(db.String(100))

# Transportation model
class Transportation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(100), nullable=False)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'), nullable=False)
    accommodation = db.Column(db.String(100), nullable=False)

# Service Animal Facility model
class ServiceAnimalFacility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
