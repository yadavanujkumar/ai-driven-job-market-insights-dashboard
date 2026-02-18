"""
Configuration module for the application.
Provides centralized configuration management with environment variable support.
"""
import os

class Config:
    """Application configuration class."""
    
    # API Configuration
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # External API Configuration
    JOB_DATA_API_URL = os.getenv('JOB_DATA_API_URL', 'https://api.example.com/job-data')
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', 30))
    
    # Indian Job Market Configuration
    MARKET_REGION = os.getenv('MARKET_REGION', 'India')
    CURRENCY = os.getenv('CURRENCY', 'INR')
    CURRENCY_SYMBOL = os.getenv('CURRENCY_SYMBOL', '₹')
    
    # Data Sources for Indian Job Market
    DATA_SOURCES = {
        'primary': 'Naukri.com, Indeed India, LinkedIn India',
        'reference': 'AmbitionBox, Glassdoor India, PayScale India',
        'note': 'Data aggregated from multiple Indian job portals and salary surveys'
    }
    
    # Cache Configuration
    CACHE_ENABLED = os.getenv('CACHE_ENABLED', 'True').lower() == 'true'
    CACHE_TTL = int(os.getenv('CACHE_TTL', 300))  # 5 minutes default
    
    # AI Model Configuration
    MODEL_TYPE = os.getenv('MODEL_TYPE', 'linear')  # linear, polynomial, or decision_tree
    POLYNOMIAL_DEGREE = int(os.getenv('POLYNOMIAL_DEGREE', 2))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')
