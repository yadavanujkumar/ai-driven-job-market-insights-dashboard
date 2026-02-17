from src.repositories.job_repository import JobRepository
from src.services.ai_model import AIModel
from src.utils.cache import Cache
from src.utils.logger import setup_logger
from src.utils.validation import ValidationError

logger = setup_logger(__name__)

class JobService:
    def __init__(self):
        self.job_repository = JobRepository()
        self.ai_model = AIModel()
        self.cache = Cache()
        logger.info("JobService initialized")

    def get_job_trends(self):
        """
        Fetch and process job market trends with caching.
        
        Returns:
            Dictionary with job market trends
        """
        cache_key = 'job_trends'
        
        # Try to get from cache first
        cached_trends = self.cache.get(cache_key)
        if cached_trends is not None:
            logger.info("Returning cached job trends")
            return cached_trends
        
        try:
            logger.info("Fetching fresh job data")
            job_data = self.job_repository.fetch_job_data()
            trends = self.ai_model.analyze_trends(job_data)
            
            # Cache the results
            self.cache.set(cache_key, trends)
            
            logger.info("Successfully analyzed job trends")
            return trends
            
        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error fetching job trends: {str(e)}")
            raise

    def predict_job_trends(self, input_data):
        """
        Predict future job trends based on input data.
        
        Args:
            input_data: Dictionary with prediction parameters
            
        Returns:
            Dictionary with predictions
        """
        try:
            logger.info("Processing prediction request")
            prediction = self.ai_model.predict(input_data)
            logger.info("Prediction completed successfully")
            return prediction
            
        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error predicting job trends: {str(e)}")
            raise
    
    def get_statistics(self):
        """
        Get aggregated statistics from job market data.
        
        Returns:
            Dictionary with overall statistics
        """
        try:
            logger.info("Fetching job statistics")
            job_data = self.job_repository.fetch_job_data()
            
            if not job_data:
                return {
                    'total_jobs': 0,
                    'message': 'No job data available'
                }
            
            # Calculate overall statistics
            salaries = [job['salary'] for job in job_data]
            categories = set(job['category'] for job in job_data)
            
            import numpy as np
            stats = {
                'total_jobs': len(job_data),
                'total_categories': len(categories),
                'categories': list(categories),
                'overall_average_salary': float(np.mean(salaries)),
                'overall_median_salary': float(np.median(salaries)),
                'salary_range': {
                    'min': float(np.min(salaries)),
                    'max': float(np.max(salaries))
                }
            }
            
            logger.info(f"Statistics calculated for {len(job_data)} jobs")
            return stats
            
        except Exception as e:
            logger.error(f"Error fetching statistics: {str(e)}")
            raise
    
    def clear_cache(self):
        """Clear all cached data."""
        self.cache.clear()
        logger.info("Cache cleared by service")
