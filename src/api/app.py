from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from src.api.routes import job_routes, dashboard_routes
from src.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Swagger UI configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "AI-Driven Job Market Insights Dashboard"}
)

# Register blueprints
app.register_blueprint(job_routes, url_prefix='/api/jobs')
app.register_blueprint(dashboard_routes, url_prefix='/')
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

logger.info("Flask application initialized")
logger.info(f"API endpoints registered under /api/jobs")
logger.info(f"Dashboard available at /")
logger.info(f"API documentation available at {SWAGGER_URL}")

if __name__ == '__main__':
    logger.info(f"Starting server on {Config.API_HOST}:{Config.API_PORT}")
    app.run(host=Config.API_HOST, port=Config.API_PORT, debug=Config.DEBUG)
