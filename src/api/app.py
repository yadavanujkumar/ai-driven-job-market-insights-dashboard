from flask import Flask
from src.api.routes import job_routes
from src.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

app = Flask(__name__)

# Register blueprints
app.register_blueprint(job_routes, url_prefix='/api/jobs')

logger.info("Flask application initialized")
logger.info(f"API endpoints registered under /api/jobs")

if __name__ == '__main__':
    logger.info(f"Starting server on {Config.API_HOST}:{Config.API_PORT}")
    app.run(host=Config.API_HOST, port=Config.API_PORT, debug=Config.DEBUG)
