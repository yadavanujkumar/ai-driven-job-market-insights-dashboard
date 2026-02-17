import numpy as np
from sklearn.linear_model import LinearRegression

class AIModel:
    def __init__(self):
        self.model = LinearRegression()

    def analyze_trends(self, job_data):
        """Analyze job market trends from data."""
        # Example: Calculate average salary per job category
        trends = {}
        for job in job_data:
            category = job['category']
            salary = job['salary']
            if category not in trends:
                trends[category] = []
            trends[category].append(salary)
        return {category: np.mean(salaries) for category, salaries in trends.items()}

    def predict(self, input_data):
        """Predict future job trends based on input data."""
        # Example: Simple linear regression prediction
        X = np.array(input_data['years']).reshape(-1, 1)
        y = np.array(input_data['salaries'])
        self.model.fit(X, y)
        future_years = np.array(input_data['future_years']).reshape(-1, 1)
        predictions = self.model.predict(future_years)
        return {'predictions': predictions.tolist()}
