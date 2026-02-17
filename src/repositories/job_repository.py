import requests
from src.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class JobRepository:
    def __init__(self):
        self.api_url = Config.JOB_DATA_API_URL
        self.timeout = Config.API_TIMEOUT
        logger.info(f"JobRepository initialized with API URL: {self.api_url}")

    def fetch_job_data(self):
        """
        Fetch job market data from an external API with fallback to mock data.
        
        Returns:
            List of job dictionaries
        """
        try:
            logger.info(f"Fetching job data from: {self.api_url}")
            response = requests.get(self.api_url, timeout=self.timeout)
            
            if response.status_code == 200:
                logger.info("Successfully fetched job data from API")
                return response.json()
            else:
                logger.warning(f"API returned status code: {response.status_code}")
                response.raise_for_status()
                
        except requests.exceptions.RequestException as e:
            logger.warning(f"Failed to fetch from API: {str(e)}. Using fallback data.")
            return self._get_fallback_data()
    
    def _get_fallback_data(self):
        """
        Provide fallback mock data when API is unavailable.
        
        Returns:
            List of job dictionaries with mock data
        """
        logger.info("Using fallback mock data")
        return [
            {'category': 'Engineering', 'salary': 95000, 'location': 'San Francisco', 'experience': '2-5 years'},
            {'category': 'Engineering', 'salary': 110000, 'location': 'New York', 'experience': '3-6 years'},
            {'category': 'Engineering', 'salary': 125000, 'location': 'Seattle', 'experience': '5-8 years'},
            {'category': 'Engineering', 'salary': 100000, 'location': 'Austin', 'experience': '2-4 years'},
            {'category': 'Data Science', 'salary': 105000, 'location': 'San Francisco', 'experience': '3-5 years'},
            {'category': 'Data Science', 'salary': 115000, 'location': 'New York', 'experience': '4-7 years'},
            {'category': 'Data Science', 'salary': 98000, 'location': 'Boston', 'experience': '2-4 years'},
            {'category': 'Marketing', 'salary': 75000, 'location': 'Chicago', 'experience': '2-5 years'},
            {'category': 'Marketing', 'salary': 85000, 'location': 'Los Angeles', 'experience': '3-6 years'},
            {'category': 'Marketing', 'salary': 80000, 'location': 'San Francisco', 'experience': '2-4 years'},
            {'category': 'Sales', 'salary': 70000, 'location': 'Dallas', 'experience': '1-3 years'},
            {'category': 'Sales', 'salary': 82000, 'location': 'Miami', 'experience': '3-5 years'},
            {'category': 'Product Management', 'salary': 120000, 'location': 'San Francisco', 'experience': '5-8 years'},
            {'category': 'Product Management', 'salary': 115000, 'location': 'Seattle', 'experience': '4-7 years'},
            {'category': 'Design', 'salary': 90000, 'location': 'New York', 'experience': '3-5 years'},
            {'category': 'Design', 'salary': 85000, 'location': 'Portland', 'experience': '2-4 years'},
        ]
