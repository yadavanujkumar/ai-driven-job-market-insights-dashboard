from flask import Blueprint, jsonify, request
from src.services.job_service import JobService

job_routes = Blueprint('job_routes', __name__)

# Initialize the service
job_service = JobService()

@job_routes.route('/trends', methods=['GET'])
def get_job_trends():
    """Endpoint to get job market trends."""
    try:
        trends = job_service.get_job_trends()
        return jsonify(trends), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@job_routes.route('/predict', methods=['POST'])
def predict_job_trends():
    """Endpoint to predict future job trends."""
    try:
        data = request.json
        prediction = job_service.predict_job_trends(data)
        return jsonify(prediction), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
