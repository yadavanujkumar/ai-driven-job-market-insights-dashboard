# API Usage Examples

This document provides examples of how to use the AI-Driven Job Market Insights Dashboard API.

## Base URL
```
http://localhost:5000/api/jobs
```

## 1. Health Check

Check if the service is running:

```bash
curl http://localhost:5000/api/jobs/health
```

Response:
```json
{
  "status": "success",
  "message": "Service is healthy",
  "service": "AI-Driven Job Market Insights Dashboard"
}
```

## 2. Get Job Market Trends

Retrieve comprehensive job market trends with statistics per category:

```bash
curl http://localhost:5000/api/jobs/trends
```

Response:
```json
{
  "status": "success",
  "data": {
    "Engineering": {
      "average_salary": 107500.0,
      "median_salary": 105000.0,
      "min_salary": 95000.0,
      "max_salary": 125000.0,
      "std_deviation": 11456.44,
      "job_count": 4
    },
    "Data Science": {
      "average_salary": 106000.0,
      "median_salary": 105000.0,
      "min_salary": 98000.0,
      "max_salary": 115000.0,
      "std_deviation": 6976.15,
      "job_count": 3
    }
  }
}
```

## 3. Get Overall Statistics

Get aggregated statistics across all job categories:

```bash
curl http://localhost:5000/api/jobs/statistics
```

Response:
```json
{
  "status": "success",
  "data": {
    "total_jobs": 16,
    "total_categories": 6,
    "categories": ["Engineering", "Data Science", "Marketing", "Sales", "Product Management", "Design"],
    "overall_average_salary": 96875.0,
    "overall_median_salary": 96500.0,
    "salary_range": {
      "min": 70000.0,
      "max": 125000.0
    }
  }
}
```

## 4. Predict Future Job Trends

Predict future salary trends based on historical data:

```bash
curl -X POST http://localhost:5000/api/jobs/predict \
  -H "Content-Type: application/json" \
  -d '{
    "years": [2020, 2021, 2022],
    "salaries": [100000, 110000, 120000],
    "future_years": [2023, 2024, 2025]
  }'
```

Response:
```json
{
  "status": "success",
  "data": {
    "predictions": [130000.0, 140000.0, 150000.0],
    "model_type": "linear",
    "confidence_score": 1.0
  }
}
```

## 5. Clear Cache

Clear all cached data to force fresh data retrieval:

```bash
curl -X POST http://localhost:5000/api/jobs/cache/clear
```

Response:
```json
{
  "status": "success",
  "message": "Cache cleared successfully"
}
```

## Error Handling

All endpoints return consistent error responses:

### Validation Error Example
```bash
curl -X POST http://localhost:5000/api/jobs/predict \
  -H "Content-Type: application/json" \
  -d '{
    "years": [2020, 2021],
    "salaries": [100000]
  }'
```

Response (400 Bad Request):
```json
{
  "status": "error",
  "error": "'years' and 'salaries' must have the same length",
  "error_type": "validation_error"
}
```

### Server Error Example

Response (500 Internal Server Error):
```json
{
  "status": "error",
  "error": "Detailed error message",
  "error_type": "server_error"
}
```

## Python Examples

### Using requests library

```python
import requests
import json

# Base URL
base_url = "http://localhost:5000/api/jobs"

# Get health status
response = requests.get(f"{base_url}/health")
print(response.json())

# Get job trends
response = requests.get(f"{base_url}/trends")
trends = response.json()
print(json.dumps(trends, indent=2))

# Get statistics
response = requests.get(f"{base_url}/statistics")
stats = response.json()
print(f"Total Jobs: {stats['data']['total_jobs']}")
print(f"Average Salary: ${stats['data']['overall_average_salary']:,.2f}")

# Make a prediction
prediction_data = {
    "years": [2020, 2021, 2022],
    "salaries": [100000, 110000, 120000],
    "future_years": [2023, 2024, 2025]
}
response = requests.post(
    f"{base_url}/predict",
    json=prediction_data
)
result = response.json()
print(f"Predictions: {result['data']['predictions']}")
print(f"Model Type: {result['data']['model_type']}")
print(f"Confidence: {result['data']['confidence_score']:.2f}")

# Clear cache
response = requests.post(f"{base_url}/cache/clear")
print(response.json()['message'])
```

## Configuration

You can configure the API using environment variables:

```bash
# Change model type (linear, polynomial, decision_tree)
export MODEL_TYPE=polynomial
export POLYNOMIAL_DEGREE=3

# Configure caching
export CACHE_ENABLED=true
export CACHE_TTL=600

# Configure logging
export LOG_LEVEL=DEBUG

# Start the application
python src/api/app.py
```
