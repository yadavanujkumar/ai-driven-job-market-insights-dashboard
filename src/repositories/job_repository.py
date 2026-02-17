import requests

class JobRepository:
    def __init__(self):
        self.api_url = 'https://api.example.com/job-data'

    def fetch_job_data(self):
        """Fetch job market data from an external API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
