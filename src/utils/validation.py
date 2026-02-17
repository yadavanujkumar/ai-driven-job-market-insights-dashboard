"""
Validation utility module.
Provides input validation functions for API endpoints.
"""
from typing import Dict, Any, List
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_prediction_input(data: Dict[str, Any]) -> None:
    """
    Validate prediction input data.
    
    Args:
        data: Input data dictionary
        
    Raises:
        ValidationError: If validation fails
    """
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    required_fields = ['years', 'salaries', 'future_years']
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
    
    # Validate years
    if not isinstance(data['years'], list) or len(data['years']) == 0:
        raise ValidationError("'years' must be a non-empty list")
    
    if not all(isinstance(year, (int, float)) for year in data['years']):
        raise ValidationError("All values in 'years' must be numbers")
    
    # Validate salaries
    if not isinstance(data['salaries'], list) or len(data['salaries']) == 0:
        raise ValidationError("'salaries' must be a non-empty list")
    
    if not all(isinstance(salary, (int, float)) for salary in data['salaries']):
        raise ValidationError("All values in 'salaries' must be numbers")
    
    if not all(salary >= 0 for salary in data['salaries']):
        raise ValidationError("All salary values must be non-negative")
    
    # Validate future_years
    if not isinstance(data['future_years'], list) or len(data['future_years']) == 0:
        raise ValidationError("'future_years' must be a non-empty list")
    
    if not all(isinstance(year, (int, float)) for year in data['future_years']):
        raise ValidationError("All values in 'future_years' must be numbers")
    
    # Validate array lengths match
    if len(data['years']) != len(data['salaries']):
        raise ValidationError("'years' and 'salaries' must have the same length")
    
    logger.debug("Prediction input validation passed")

def validate_job_data(job_data: List[Dict[str, Any]]) -> None:
    """
    Validate job data structure.
    
    Args:
        job_data: List of job data dictionaries
        
    Raises:
        ValidationError: If validation fails
    """
    if not isinstance(job_data, list):
        raise ValidationError("Job data must be a list")
    
    if len(job_data) == 0:
        raise ValidationError("Job data cannot be empty")
    
    for idx, job in enumerate(job_data):
        if not isinstance(job, dict):
            raise ValidationError(f"Job at index {idx} must be a dictionary")
        
        if 'category' not in job:
            raise ValidationError(f"Job at index {idx} missing 'category' field")
        
        if 'salary' not in job:
            raise ValidationError(f"Job at index {idx} missing 'salary' field")
        
        if not isinstance(job['salary'], (int, float)):
            raise ValidationError(f"Salary at index {idx} must be a number")
        
        if job['salary'] < 0:
            raise ValidationError(f"Salary at index {idx} must be non-negative")
    
    logger.debug(f"Job data validation passed for {len(job_data)} jobs")
