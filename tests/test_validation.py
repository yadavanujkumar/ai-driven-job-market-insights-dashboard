import unittest
from src.utils.validation import validate_prediction_input, validate_job_data, ValidationError

class TestValidation(unittest.TestCase):

    def test_validate_prediction_input_valid(self):
        """Test validation passes for valid prediction input."""
        data = {
            'years': [2020, 2021, 2022],
            'salaries': [100000, 110000, 120000],
            'future_years': [2023, 2024]
        }
        # Should not raise exception
        validate_prediction_input(data)

    def test_validate_prediction_input_missing_field(self):
        """Test validation fails for missing required field."""
        data = {
            'years': [2020, 2021],
            'salaries': [100000, 110000]
        }
        with self.assertRaises(ValidationError) as context:
            validate_prediction_input(data)
        self.assertIn('future_years', str(context.exception))

    def test_validate_prediction_input_empty_list(self):
        """Test validation fails for empty lists."""
        data = {
            'years': [],
            'salaries': [100000],
            'future_years': [2023]
        }
        with self.assertRaises(ValidationError):
            validate_prediction_input(data)

    def test_validate_prediction_input_negative_salary(self):
        """Test validation fails for negative salaries."""
        data = {
            'years': [2020, 2021],
            'salaries': [100000, -50000],
            'future_years': [2023]
        }
        with self.assertRaises(ValidationError) as context:
            validate_prediction_input(data)
        self.assertIn('non-negative', str(context.exception))

    def test_validate_prediction_input_length_mismatch(self):
        """Test validation fails when years and salaries length don't match."""
        data = {
            'years': [2020, 2021],
            'salaries': [100000],
            'future_years': [2023]
        }
        with self.assertRaises(ValidationError) as context:
            validate_prediction_input(data)
        self.assertIn('same length', str(context.exception))

    def test_validate_job_data_valid(self):
        """Test validation passes for valid job data."""
        job_data = [
            {'category': 'Engineering', 'salary': 100000},
            {'category': 'Marketing', 'salary': 80000}
        ]
        # Should not raise exception
        validate_job_data(job_data)

    def test_validate_job_data_empty(self):
        """Test validation fails for empty job data."""
        with self.assertRaises(ValidationError):
            validate_job_data([])

    def test_validate_job_data_missing_category(self):
        """Test validation fails for missing category."""
        job_data = [
            {'salary': 100000}
        ]
        with self.assertRaises(ValidationError) as context:
            validate_job_data(job_data)
        self.assertIn('category', str(context.exception))

    def test_validate_job_data_missing_salary(self):
        """Test validation fails for missing salary."""
        job_data = [
            {'category': 'Engineering'}
        ]
        with self.assertRaises(ValidationError) as context:
            validate_job_data(job_data)
        self.assertIn('salary', str(context.exception))

    def test_validate_job_data_negative_salary(self):
        """Test validation fails for negative salary."""
        job_data = [
            {'category': 'Engineering', 'salary': -50000}
        ]
        with self.assertRaises(ValidationError) as context:
            validate_job_data(job_data)
        self.assertIn('non-negative', str(context.exception))
