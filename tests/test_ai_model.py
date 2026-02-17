import unittest
from src.services.ai_model import AIModel

class TestAIModel(unittest.TestCase):

    def test_analyze_trends(self):
        model = AIModel()
        job_data = [
            {'category': 'Engineering', 'salary': 100000},
            {'category': 'Engineering', 'salary': 120000},
            {'category': 'Marketing', 'salary': 80000}
        ]
        trends = model.analyze_trends(job_data)
        self.assertEqual(trends, {'Engineering': 110000, 'Marketing': 80000})

    def test_predict(self):
        model = AIModel()
        input_data = {
            'years': [2020, 2021, 2022],
            'salaries': [100000, 110000, 120000],
            'future_years': [2023, 2024]
        }
        predictions = model.predict(input_data)
        self.assertIn('predictions', predictions)
        self.assertEqual(len(predictions['predictions']), 2)
