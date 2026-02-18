# AI-Driven Indian Job Market Insights Dashboard

A comprehensive web application for analyzing **Indian job market** trends and making predictions using AI/ML models. Available as both a **Streamlit interactive app** and a **Flask RESTful API** with Swagger documentation.

**All salary data is in Indian Rupees (₹) and based on real salary surveys from Indian job portals.**

## 🚀 Quick Start

### Option 1: Streamlit Application (Recommended)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit App**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the Dashboard**
   - Streamlit Dashboard: http://localhost:8501

### Option 2: Flask API + Web Dashboard

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask Application**
   ```bash
   python src/api/app.py
   ```

3. **Access the Dashboard**
   - Web Dashboard: http://localhost:5000/
   - Interactive Dashboard: http://localhost:5000/dashboard
   - API Documentation: http://localhost:5000/api/docs

## System Architecture

The system is designed using a modular, layered architecture to ensure scalability, maintainability, and testability. The key components are:

1. **Web Dashboard**: Interactive web interface with real-time data visualization using Chart.js
2. **API Layer**: RESTful endpoints with CORS support and comprehensive error handling
3. **Service Layer**: Business logic for processing job market data and generating insights with caching support
4. **Repository Layer**: Data access and storage, including integration with external APIs and fallback mechanisms
5. **AI Module**: Multiple machine learning models (Linear Regression, Polynomial Regression, Decision Tree) for trend analysis and predictions
6. **Utilities**: Logging, caching, and validation modules for enhanced reliability and performance
7. **Testing**: Comprehensive unit tests ensure the reliability of the system

### Directory Structure

- `src/api/`: API routes, controllers, static files, and templates
  - `templates/`: HTML templates for the web dashboard
  - `static/`: Static files including Swagger/OpenAPI specification
- `src/services/`: Business logic and AI processing
- `src/repositories/`: Data access and external API integrations
- `src/utils/`: Utility modules (logging, caching, validation)
- `src/config.py`: Centralized configuration management
- `tests/`: Comprehensive unit tests for all modules
- `Dockerfile`: Docker configuration for containerization
- `requirements.txt`: Python dependencies

### Features

- **🇮🇳 Indian Job Market Focus**: Data tailored for Indian job market with salaries in INR (₹)
- **📊 Real Data Sources**: Based on actual salary surveys from Naukri.com, Indeed India, LinkedIn India, AmbitionBox, Glassdoor India
- **🎨 Interactive Web Dashboard**: Beautiful, responsive UI with real-time data visualization
- **📊 Data Visualization**: Interactive charts and graphs using Chart.js and Plotly
- **🤖 Advanced AI Models**: Multiple ML algorithms (Linear, Polynomial, Decision Tree) for predictions
- **📈 Comprehensive Trend Analysis**: Detailed statistics including mean, median, min, max, standard deviation
- **⚡ Intelligent Caching**: In-memory caching with configurable TTL for improved performance
- **✅ Input Validation**: Robust validation for all API inputs with detailed error messages
- **📝 Logging System**: Structured logging for better observability and debugging
- **🔄 Real Market Data**: Salaries based on 2023-2024 salary surveys from Indian job portals
- **💰 Currency Transparency**: All amounts clearly displayed in Indian Rupees (₹)
- **📚 Data Attribution**: Clear references to data sources for transparency
- **💚 Health Monitoring**: Health check endpoint for service monitoring
- **📊 Statistics Endpoint**: Aggregated job market statistics across all categories
- **🌐 RESTful API**: Clean, well-documented API with consistent response formats
- **📚 Swagger Documentation**: Interactive API documentation with Swagger UI
- **🔓 CORS Support**: Cross-Origin Resource Sharing enabled for web clients
- **🐳 Dockerized**: Easy deployment with Docker containerization

## Data Sources

### Primary Sources
- **Naukri.com**: India's leading job portal
- **Indeed India**: Major international job portal with Indian market data
- **LinkedIn India**: Professional networking platform with salary insights

### Reference Sources
- **AmbitionBox**: Salary insights and company reviews
- **Glassdoor India**: Employee reviews and salary data
- **PayScale India**: Salary comparison and career information

### Data Quality
- **Survey Period**: 2023-2024
- **Market**: Indian tech and corporate sectors
- **Currency**: All salaries in Indian Rupees (₹ INR) per annum
- **Locations**: Major Indian cities including Bangalore, Hyderabad, Pune, Mumbai, Gurgaon, Delhi
- **Disclaimer**: Salary ranges are indicative. Actual offers may vary based on company, skills, and negotiation.

## Web Dashboard

### Landing Page
The landing page (http://localhost:5000/) provides:
- Overview of system features
- Quick access to dashboard and API documentation
- List of available API endpoints
- Modern, gradient design with card-based layout

### Interactive Dashboard
The main dashboard includes:
- **Indian Market Statistics**: Total jobs, categories, average salary in INR (₹)
- **Salary Chart**: Bar chart showing average salaries by job category in INR
- **Distribution Chart**: Doughnut chart displaying job distribution across categories
- **Category Details**: Comprehensive statistics for each job category
- **Data Sources Display**: Clear attribution of data sources
- **Prediction Interface**: Interactive form to predict future salary trends with AI (in INR)

### Streamlit Dashboard
The Streamlit app (http://localhost:8501) provides:
- **Indian Market Overview**: Key metrics and visualizations with INR currency
- **Data Source Information**: Expandable section showing all data sources and references
- **Trends Analysis**: Deep dive into specific job categories
- **Salary Prediction**: AI-powered forecasting with Indian market data
- **Interactive Charts**: Plotly visualizations with hover details

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
Returns comprehensive Indian job market trends with statistics per category:
- Average, median, min, max salaries (in INR)
- Standard deviation
- Job count per category
- Market metadata (region, currency, data sources)

Example response:
```json
{
  "status": "success",
  "data": {
    "trends": {
      "Software Engineering": {
        "average_salary": 1650000.0,
        "median_salary": 1550000.0,
        "min_salary": 1000000.0,
        "max_salary": 2500000.0,
        "std_deviation": 469041.58,
        "job_count": 8
      }
    },
    "metadata": {
      "region": "India",
      "currency": "INR",
      "currency_symbol": "₹",
      "data_sources": {
        "primary": "Naukri.com, Indeed India, LinkedIn India",
        "reference": "AmbitionBox, Glassdoor India, PayScale India"
      }
    }
  }
}
```

#### 3. Get Statistics
```bash
GET /api/jobs/statistics
```
Returns overall Indian job market statistics:
- Total jobs and categories
- Overall average and median salary (in INR)
- Salary range
- Market metadata and data sources

#### 4. Predict Job Trends
```bash
POST /api/jobs/predict
Content-Type: application/json

{
  "years": [2020, 2021, 2022, 2023],
  "salaries": [1000000, 1150000, 1300000, 1450000],
  "future_years": [2024, 2025, 2026]
}
```
Predict future salary trends based on historical Indian market data (salaries in INR).
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
- `JOB_DATA_API_URL`: External API URL for real-time data
- `API_TIMEOUT`: API request timeout in seconds (default: 30)
- `MARKET_REGION`: Market region (default: 'India')
- `CURRENCY`: Currency code (default: 'INR')
- `CURRENCY_SYMBOL`: Currency symbol (default: '₹')
- `CACHE_ENABLED`: Enable/disable caching (default: True)
- `CACHE_TTL`: Cache time-to-live in seconds (default: 300)
- `MODEL_TYPE`: AI model type - 'linear', 'polynomial', or 'decision_tree' (default: 'linear')
- `POLYNOMIAL_DEGREE`: Degree for polynomial regression (default: 2)
- `LOG_LEVEL`: Logging level (default: 'INFO')

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-driven-job-market-insights-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python src/api/app.py
   ```

4. **Access the application**
   - Landing Page: http://localhost:5000/
   - Dashboard: http://localhost:5000/dashboard
   - API Documentation: http://localhost:5000/api/docs
   - API Base: http://localhost:5000/api/jobs

5. **Run tests**
   ```bash
   PYTHONPATH=. pytest tests/ -v
   ```

### Docker Deployment

**Flask Version:**
```bash
docker build -t job-insights-dashboard .
docker run -p 5000:5000 job-insights-dashboard
```

Access the dashboard at http://localhost:5000/

### Streamlit Cloud Deployment

The Streamlit app can be easily deployed to Streamlit Cloud:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Streamlit deployment"
   git push
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set the main file path to: `streamlit_app.py`
   - Click "Deploy"

3. **Configuration**
   - The app uses `.streamlit/config.toml` for configuration
   - No additional secrets or configuration needed for basic deployment

### Local Streamlit Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

# Run on a specific port
streamlit run streamlit_app.py --server.port 8502

# Run in development mode with auto-reload
streamlit run streamlit_app.py --server.runOnSave true
```

Access the Streamlit app at http://localhost:8501

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

## What's New

### Version 3.0 - Indian Market Edition (2024)

🇮🇳 **Major Update: Complete Indian Job Market Focus**

This version transforms the dashboard into a specialized tool for the Indian job market:

**New Features:**
- **Indian Market Data**: All salary data in Indian Rupees (₹ INR)
- **Real Data Sources**: Based on actual salary surveys from Indian job portals
- **Data Attribution**: Clear references to Naukri.com, Indeed India, LinkedIn India, AmbitionBox, Glassdoor India
- **Indian Cities**: Data from Bangalore, Hyderabad, Pune, Mumbai, Gurgaon, Delhi
- **Company Types**: Differentiation between Product, Service, Startup, and Enterprise companies
- **Enhanced Job Categories**: 
  - Software Engineering
  - Data Science
  - Product Management
  - UI/UX Design
  - Digital Marketing
  - Sales & Business Development
  - DevOps
  - Quality Assurance
- **Metadata Support**: Every API response includes region, currency, and data source information
- **Salary Ranges**: 7 LPA to 25 LPA based on real market surveys (2023-2024)
- **Experience Brackets**: Realistic experience ranges for Indian market
- **Transparency**: Full disclaimer and data quality information displayed

**Technical Improvements:**
- Updated data structure to include comprehensive metadata
- Fixed datetime deprecation warnings
- Enhanced test coverage for new data format
- Added configuration options for market region and currency
- Improved data source documentation

### Version 2.1 - Streamlit Edition

🎉 **Major Addition: Streamlit Application**

The dashboard is now available as an interactive Streamlit application, making it even easier to deploy and use!

✨ **Streamlit Features:**
- **Modern Interactive UI**: Built with Streamlit for a smooth, reactive user experience
- **Real-time Visualizations**: Interactive Plotly charts (bar charts, pie charts, box plots, gauges)
- **Multi-page Navigation**: Separate pages for Dashboard, Trends Analysis, and Predictions
- **Easy Deployment**: One-click deployment to Streamlit Cloud
- **Cache Management**: Built-in cache control for optimal performance
- **Responsive Design**: Works seamlessly on desktop and mobile devices

🚀 **Deployment Options:**
1. **Streamlit App** (NEW): `streamlit run streamlit_app.py` - Recommended for quick deployment
2. **Flask API**: `python src/api/app.py` - For programmatic access and custom integrations

📊 **Streamlit Pages:**
- **Dashboard**: Overview with key metrics and visualizations
- **Trends Analysis**: Deep dive into specific job categories
- **Salary Prediction**: AI-powered salary forecasting
- **About**: Information about the application and features

### Version 2.0 - Interactive Dashboard Update

This version transforms the application from a basic API-only service to a full-featured web application:

✨ **New Features:**
- **Interactive Web Dashboard**: Beautiful, responsive UI with gradient design and modern aesthetics
- **Real-time Data Visualization**: Interactive charts using Chart.js (bar charts for salaries, doughnut charts for distribution)
- **Landing Page**: Professional landing page with feature highlights and API overview
- **Swagger UI Integration**: Interactive API documentation at `/api/docs`
- **CORS Support**: Enabled Cross-Origin Resource Sharing for web clients
- **Enhanced User Experience**: Prediction interface with real-time feedback and loading states

🎨 **Design Improvements:**
- Modern gradient color scheme (purple to violet)
- Responsive card-based layout
- Interactive hover effects and animations
- Clean, professional typography
- Mobile-friendly responsive design

📊 **Dashboard Features:**
- Live statistics cards (total jobs, categories, salaries)
- Interactive salary comparison charts
- Job distribution visualization
- Category-wise detailed statistics
- AI-powered prediction interface
- Real-time data fetching and updates

### Future Enhancements

- Connect to live APIs from Indian job portals (with authentication)
- Add database persistence for historical trend tracking
- Implement user authentication and role-based access control
- Integrate with additional Indian job market data sources (Monster India, TimesJobs)
- Add more advanced AI models (LSTM, Prophet for time series)
- City-wise salary comparison and cost-of-living adjustments
- Skill-based salary insights and recommendations
- Company-wise salary distributions
- Implement WebSocket support for real-time updates
- Export functionality for charts and data (PDF, Excel)
- Email alerts for salary trend changes
- Integration with Indian tax calculator for take-home salary
- Career path recommendations based on market trends
