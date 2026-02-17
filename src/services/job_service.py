from src.repositories.job_repository import JobRepository
from src.services.ai_model import AIModel

class JobService:
    def __init__(self):
        self.job_repository = JobRepository()
        self.ai_model = AIModel()

    def get_job_trends(self):
        """Fetch and process job market trends."""
        job_data = self.job_repository.fetch_job_data()
        trends = self.ai_model.analyze_trends(job_data)
        return trends

    def predict_job_trends(self, input_data):
        """Predict future job trends based on input data."""
        prediction = self.ai_model.predict(input_data)
        return prediction
