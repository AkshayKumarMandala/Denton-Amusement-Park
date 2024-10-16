from flask import Blueprint, request, jsonify
from app import db
from app.models import Feedback

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/feedbacks', methods=['GET'])
def get_feedbacks():
    feedbacks = Feedback.query.all()
    return jsonify([feedback.message for feedback in feedbacks])

@admin_bp.route('/admin/respond', methods=['POST'])
def respond_to_feedback():
    data = request.json
    # Logic for responding to feedback
    return jsonify({'status': 'success'})
