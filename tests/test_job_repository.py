import unittest
from unittest.mock import patch, MagicMock
from src.repositories.job_repository import JobRepository
import requests

class TestJobRepository(unittest.TestCase):

    @patch('src.repositories.job_repository.requests.get')
    def test_fetch_job_data_success(self, mock_get):
        """Test successful API data fetch."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'category': 'Engineering', 'salary': 100000}
        ]
        mock_get.return_value = mock_response
        
        repo = JobRepository()
        data = repo.fetch_job_data()
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['category'], 'Engineering')

    @patch('src.repositories.job_repository.requests.get')
    def test_fetch_job_data_fallback(self, mock_get):
        """Test fallback to mock data on API failure."""
        mock_get.side_effect = requests.exceptions.RequestException("API Error")
        
        repo = JobRepository()
        data = repo.fetch_job_data()
        
        # Should return fallback data
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('category', data[0])
        self.assertIn('salary', data[0])

    @patch('src.repositories.job_repository.requests.get')
    def test_fetch_job_data_http_error(self, mock_get):
        """Test fallback on HTTP error."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Error")
        mock_get.return_value = mock_response
        
        repo = JobRepository()
        data = repo.fetch_job_data()
        
        # Should return fallback data
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
