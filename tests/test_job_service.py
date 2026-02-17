import unittest
from unittest.mock import patch
from src.services.job_service import JobService

class TestJobService(unittest.TestCase):

    @patch('src.repositories.job_repository.JobRepository.fetch_job_data')
    @patch('src.services.ai_model.AIModel.analyze_trends')
    def test_get_job_trends(self, mock_analyze_trends, mock_fetch_job_data):
        mock_fetch_job_data.return_value = [
            {'category': 'Engineering', 'salary': 100000},
            {'category': 'Engineering', 'salary': 120000},
            {'category': 'Marketing', 'salary': 80000}
        ]
        mock_analyze_trends.return_value = {'Engineering': 110000, 'Marketing': 80000}

        service = JobService()
        trends = service.get_job_trends()

        self.assertEqual(trends, {'Engineering': 110000, 'Marketing': 80000})

    @patch('src.services.ai_model.AIModel.predict')
    def test_predict_job_trends(self, mock_predict):
        mock_predict.return_value = {'predictions': [130000, 140000]}

        service = JobService()
        input_data = {
            'years': [2020, 2021, 2022],
            'salaries': [100000, 110000, 120000],
            'future_years': [2023, 2024]
        }
        prediction = service.predict_job_trends(input_data)

        self.assertEqual(prediction, {'predictions': [130000, 140000]})
