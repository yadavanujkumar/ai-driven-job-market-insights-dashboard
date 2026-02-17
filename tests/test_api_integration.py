import unittest
from src.api.app import app

class TestAPIIntegration(unittest.TestCase):

    def setUp(self):
        """Set up test client."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client.get('/api/jobs/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('Service is healthy', data['message'])

    def test_get_trends(self):
        """Test get trends endpoint."""
        response = self.client.get('/api/jobs/trends')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        # Should have multiple categories
        self.assertGreater(len(data['data']), 0)
        # Check structure of first category
        first_category = list(data['data'].values())[0]
        self.assertIn('average_salary', first_category)
        self.assertIn('job_count', first_category)

    def test_get_statistics(self):
        """Test get statistics endpoint."""
        response = self.client.get('/api/jobs/statistics')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('total_jobs', data['data'])
        self.assertIn('total_categories', data['data'])
        self.assertIn('overall_average_salary', data['data'])

    def test_predict_valid(self):
        """Test predict endpoint with valid data."""
        payload = {
            'years': [2020, 2021, 2022],
            'salaries': [100000, 110000, 120000],
            'future_years': [2023, 2024]
        }
        response = self.client.post(
            '/api/jobs/predict',
            json=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('predictions', data['data'])
        self.assertEqual(len(data['data']['predictions']), 2)
        self.assertIn('model_type', data['data'])
        self.assertIn('confidence_score', data['data'])

    def test_predict_invalid_missing_field(self):
        """Test predict endpoint with missing field."""
        payload = {
            'years': [2020, 2021],
            'salaries': [100000, 110000]
            # missing future_years
        }
        response = self.client.post(
            '/api/jobs/predict',
            json=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['error_type'], 'validation_error')

    def test_predict_invalid_length_mismatch(self):
        """Test predict endpoint with length mismatch."""
        payload = {
            'years': [2020, 2021, 2022],
            'salaries': [100000, 110000],
            'future_years': [2023]
        }
        response = self.client.post(
            '/api/jobs/predict',
            json=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('same length', data['error'])

    def test_predict_no_json(self):
        """Test predict endpoint without JSON data."""
        response = self.client.post('/api/jobs/predict')
        # Flask returns 500 when Content-Type is not set properly
        self.assertIn(response.status_code, [400, 500])
        data = response.get_json()
        self.assertEqual(data['status'], 'error')

    def test_clear_cache(self):
        """Test clear cache endpoint."""
        response = self.client.post('/api/jobs/cache/clear')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('Cache cleared', data['message'])
