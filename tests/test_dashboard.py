import unittest
from src.api.app import app


class TestDashboardRoutes(unittest.TestCase):
    """Test cases for dashboard routes"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
    
    def test_landing_page(self):
        """Test landing page renders successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AI-Driven Job Market Insights', response.data)
        self.assertIn(b'Dashboard', response.data)
    
    def test_dashboard_page(self):
        """Test dashboard page renders successfully"""
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)
        self.assertIn(b'chart', response.data.lower())
    
    def test_cors_headers(self):
        """Test CORS headers are present"""
        response = self.client.get('/api/jobs/health')
        self.assertEqual(response.status_code, 200)
        # CORS headers should be present
        self.assertIn('Access-Control-Allow-Origin', response.headers)


if __name__ == '__main__':
    unittest.main()
