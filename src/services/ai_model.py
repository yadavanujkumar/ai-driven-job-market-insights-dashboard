import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from src.config import Config
from src.utils.logger import setup_logger
from src.utils.validation import validate_job_data, validate_prediction_input, ValidationError

logger = setup_logger(__name__)

class AIModel:
    def __init__(self, model_type: str = None):
        """
        Initialize AI model with specified algorithm.
        
        Args:
            model_type: Type of model ('linear', 'polynomial', 'decision_tree')
        """
        self.model_type = model_type or Config.MODEL_TYPE
        self.model = self._create_model()
        self.poly_features = None
        
        if self.model_type == 'polynomial':
            self.poly_features = PolynomialFeatures(degree=Config.POLYNOMIAL_DEGREE)
        
        logger.info(f"Initialized AI model with type: {self.model_type}")
    
    def _create_model(self):
        """Create model instance based on model_type."""
        if self.model_type == 'linear':
            return LinearRegression()
        elif self.model_type == 'polynomial':
            return LinearRegression()
        elif self.model_type == 'decision_tree':
            return DecisionTreeRegressor(random_state=42, max_depth=5)
        else:
            logger.warning(f"Unknown model type: {self.model_type}, defaulting to linear")
            return LinearRegression()

    def analyze_trends(self, job_data):
        """
        Analyze job market trends from data.
        
        Args:
            job_data: List of job dictionaries with 'category' and 'salary' keys
            
        Returns:
            Dictionary with statistics per category
        """
        try:
            validate_job_data(job_data)
        except ValidationError as e:
            logger.error(f"Validation error in analyze_trends: {str(e)}")
            raise
        
        # Calculate comprehensive statistics per job category
        trends = {}
        for job in job_data:
            category = job['category']
            salary = job['salary']
            if category not in trends:
                trends[category] = {
                    'salaries': [],
                    'count': 0
                }
            trends[category]['salaries'].append(salary)
            trends[category]['count'] += 1
        
        # Compute statistics
        result = {}
        for category, data in trends.items():
            salaries = np.array(data['salaries'])
            result[category] = {
                'average_salary': float(np.mean(salaries)),
                'median_salary': float(np.median(salaries)),
                'min_salary': float(np.min(salaries)),
                'max_salary': float(np.max(salaries)),
                'std_deviation': float(np.std(salaries)),
                'job_count': data['count']
            }
        
        logger.info(f"Analyzed trends for {len(result)} categories")
        return result

    def predict(self, input_data):
        """
        Predict future job trends based on input data.
        
        Args:
            input_data: Dictionary with 'years', 'salaries', and 'future_years' keys
            
        Returns:
            Dictionary with predictions and model information
        """
        try:
            validate_prediction_input(input_data)
        except ValidationError as e:
            logger.error(f"Validation error in predict: {str(e)}")
            raise
        
        X = np.array(input_data['years']).reshape(-1, 1)
        y = np.array(input_data['salaries'])
        future_years = np.array(input_data['future_years']).reshape(-1, 1)
        
        # Apply polynomial features if needed
        if self.model_type == 'polynomial' and self.poly_features:
            X = self.poly_features.fit_transform(X)
            future_years = self.poly_features.transform(future_years)
        
        # Train model
        self.model.fit(X, y)
        
        # Make predictions
        predictions = self.model.predict(future_years)
        
        # Calculate confidence score (R² score on training data)
        score = self.model.score(X, y)
        
        result = {
            'predictions': predictions.tolist(),
            'model_type': self.model_type,
            'confidence_score': float(score)
        }
        
        logger.info(f"Prediction completed with {self.model_type} model, confidence: {score:.3f}")
        return result
