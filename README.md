# AI-Driven Job Market Insights Dashboard

## System Architecture

The system is designed using a modular, layered architecture to ensure scalability, maintainability, and testability. The key components are:

1. **API Layer**: Exposes RESTful endpoints for interacting with the system with comprehensive error handling.
2. **Service Layer**: Contains business logic for processing job market data and generating insights with caching support.
3. **Repository Layer**: Handles data access and storage, including integration with external APIs and fallback mechanisms.
4. **AI Module**: Implements multiple machine learning models (Linear Regression, Polynomial Regression, Decision Tree) for trend analysis and predictions.
5. **Utilities**: Logging, caching, and validation modules for enhanced reliability and performance.
6. **Testing**: Comprehensive unit tests ensure the reliability of the system.

### Directory Structure

- `src/api/`: Contains API routes and controllers.
- `src/services/`: Contains business logic and AI processing.
- `src/repositories/`: Handles data access and external API integrations.
- `src/utils/`: Utility modules (logging, caching, validation).
- `src/config.py`: Centralized configuration management.
- `tests/`: Contains unit tests for all modules.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: Python dependencies.

### Features

- **Advanced AI Models**: Multiple ML algorithms (Linear, Polynomial, Decision Tree) for predictions
- **Comprehensive Trend Analysis**: Detailed statistics including mean, median, min, max, standard deviation
- **Intelligent Caching**: In-memory caching with configurable TTL for improved performance
- **Input Validation**: Robust validation for all API inputs with detailed error messages
- **Logging System**: Structured logging for better observability and debugging
- **Fallback Data**: Automatic fallback to mock data when external API is unavailable
- **Health Monitoring**: Health check endpoint for service monitoring
- **Statistics Endpoint**: Aggregated job market statistics across all categories
- **RESTful API**: Clean, well-documented API with consistent response formats
- **Dockerized**: Easy deployment with Docker containerization

### API Endpoints

#### 1. Health Check
```bash
GET /api/jobs/health
```
Returns service health status.

#### 2. Get Job Trends
```bash
GET /api/jobs/trends
```
Returns comprehensive job market trends with statistics per category:
- Average, median, min, max salaries
- Standard deviation
- Job count per category

#### 3. Get Statistics
```bash
GET /api/jobs/statistics
```
Returns overall job market statistics:
- Total jobs and categories
- Overall average and median salary
- Salary range

#### 4. Predict Job Trends
```bash
POST /api/jobs/predict
Content-Type: application/json

{
  "years": [2020, 2021, 2022],
  "salaries": [100000, 110000, 120000],
  "future_years": [2023, 2024, 2025]
}
```
Returns predictions with model type and confidence score.

#### 5. Clear Cache
```bash
POST /api/jobs/cache/clear
```
Clears all cached data.

### Configuration

The application supports configuration via environment variables:

- `API_HOST`: Host address (default: '0.0.0.0')
- `API_PORT`: Port number (default: 5000)
- `DEBUG`: Debug mode (default: True)
- `JOB_DATA_API_URL`: External API URL
- `API_TIMEOUT`: API request timeout in seconds (default: 30)
- `CACHE_ENABLED`: Enable/disable caching (default: True)
- `CACHE_TTL`: Cache time-to-live in seconds (default: 300)
- `MODEL_TYPE`: AI model type - 'linear', 'polynomial', or 'decision_tree' (default: 'linear')
- `POLYNOMIAL_DEGREE`: Degree for polynomial regression (default: 2)
- `LOG_LEVEL`: Logging level (default: 'INFO')

### Setup Instructions

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the application: `python src/api/app.py`.
4. Run tests: `PYTHONPATH=. pytest tests/`.

### Docker Deployment

```bash
docker build -t job-insights-dashboard .
docker run -p 5000:5000 job-insights-dashboard
```

### Testing

The project includes comprehensive unit tests covering:
- AI model functionality (trend analysis, predictions)
- Service layer logic (caching, error handling)
- Repository layer (API integration, fallback data)
- Validation logic
- Cache operations

Run tests with:
```bash
PYTHONPATH=. pytest tests/ -v
```

### Future Enhancements

- Add database persistence for historical data
- Implement user authentication and role-based access control
- Integrate with additional job market data sources
- Add more advanced AI models (LSTM, Prophet for time series)
- Implement WebSocket support for real-time updates
- Add data visualization dashboard
