from flask import Blueprint, jsonify, request
from src.services.job_service import JobService
from src.utils.validation import ValidationError
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

job_routes = Blueprint('job_routes', __name__)

# Initialize the service
job_service = JobService()

@job_routes.route('/trends', methods=['GET'])
def get_job_trends():
    """
    Endpoint to get job market trends.
    
    Returns comprehensive statistics per job category including:
    - Average, median, min, max salaries
    - Standard deviation
    - Job count per category
    """
    try:
        logger.info("Received request for job trends")
        trends = job_service.get_job_trends()
        return jsonify({
            'status': 'success',
            'data': trends
        }), 200
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'validation_error'
        }), 400
    except Exception as e:
        logger.error(f"Error in get_job_trends: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'server_error'
        }), 500

@job_routes.route('/predict', methods=['POST'])
def predict_job_trends():
    """
    Endpoint to predict future job trends.
    
    Expects JSON body with:
    - years: List of historical years
    - salaries: List of corresponding salaries
    - future_years: List of years to predict
    
    Returns predictions with model information and confidence score.
    """
    try:
        data = request.json
        
        if not data:
            return jsonify({
                'status': 'error',
                'error': 'No JSON data provided',
                'error_type': 'validation_error'
            }), 400
        
        logger.info("Received prediction request")
        prediction = job_service.predict_job_trends(data)
        return jsonify({
            'status': 'success',
            'data': prediction
        }), 200
        
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'validation_error'
        }), 400
    except Exception as e:
        logger.error(f"Error in predict_job_trends: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'server_error'
        }), 500

@job_routes.route('/statistics', methods=['GET'])
def get_statistics():
    """
    Endpoint to get overall job market statistics.
    
    Returns aggregated statistics including:
    - Total number of jobs
    - Total categories
    - Overall average and median salary
    - Salary range
    """
    try:
        logger.info("Received request for statistics")
        stats = job_service.get_statistics()
        return jsonify({
            'status': 'success',
            'data': stats
        }), 200
    except Exception as e:
        logger.error(f"Error in get_statistics: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'server_error'
        }), 500

@job_routes.route('/cache/clear', methods=['POST'])
def clear_cache():
    """
    Endpoint to clear the cache.
    
    Useful for forcing fresh data retrieval.
    """
    try:
        logger.info("Received request to clear cache")
        job_service.clear_cache()
        return jsonify({
            'status': 'success',
            'message': 'Cache cleared successfully'
        }), 200
    except Exception as e:
        logger.error(f"Error in clear_cache: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e),
            'error_type': 'server_error'
        }), 500

@job_routes.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    Returns the health status of the service.
    """
    return jsonify({
        'status': 'success',
        'message': 'Service is healthy',
        'service': 'AI-Driven Job Market Insights Dashboard'
    }), 200
