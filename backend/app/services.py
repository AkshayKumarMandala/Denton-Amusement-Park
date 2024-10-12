from app.models import Service, db

# Service to fetch all services
def fetch_all_services():
    return Service.query.all()

# Service to add a new service
def add_new_service(name, description):
    new_service = Service(name=name, description=description)
    db.session.add(new_service)
    db.session.commit()
    return new_service