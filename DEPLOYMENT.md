# Streamlit Deployment Guide

This guide provides instructions for deploying the AI-Driven Job Market Insights Dashboard using Streamlit.

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

Access the dashboard at http://localhost:8501

## Deployment Options

### 1. Streamlit Cloud (Recommended)

Streamlit Cloud offers free hosting for Streamlit apps:

1. **Push your code to GitHub** (already done!)

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Sign in with your GitHub account**

4. **Click "New app"**

5. **Fill in the deployment form:**
   - Repository: `yadavanujkumar/ai-driven-job-market-insights-dashboard`
   - Branch: `copilot/make-streamlit-deployable` (or your merged branch)
   - Main file path: `streamlit_app.py`

6. **Click "Deploy"**

Your app will be live in a few minutes at a URL like:
`https://your-app-name.streamlit.app`

### 2. Docker Deployment

You can containerize the Streamlit app:

```dockerfile
# Dockerfile for Streamlit
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t job-insights-streamlit .
docker run -p 8501:8501 job-insights-streamlit
```

### 3. Heroku Deployment

Create a `setup.sh` file:
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

Create a `Procfile`:
```
web: sh setup.sh && streamlit run streamlit_app.py
```

Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### 4. AWS EC2 / Azure VM

On your server:

```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# Run with nohup for background execution
nohup streamlit run streamlit_app.py --server.port=8501 &

# Or use systemd service
sudo nano /etc/systemd/system/streamlit.service
```

Systemd service file:
```ini
[Unit]
Description=Streamlit Job Insights Dashboard
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/ai-driven-job-market-insights-dashboard
ExecStart=/usr/local/bin/streamlit run streamlit_app.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable streamlit
sudo systemctl start streamlit
```

## Configuration

The app uses `.streamlit/config.toml` for configuration:

```toml
[theme]
primaryColor = "#8B5CF6"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

## Environment Variables

You can configure the app using environment variables:

- `API_HOST`: Host address (default: '0.0.0.0')
- `API_PORT`: Port number (default: 5000) - for Flask API
- `DEBUG`: Debug mode (default: True)
- `JOB_DATA_API_URL`: External API URL
- `API_TIMEOUT`: API request timeout in seconds (default: 30)
- `CACHE_ENABLED`: Enable/disable caching (default: True)
- `CACHE_TTL`: Cache time-to-live in seconds (default: 300)
- `MODEL_TYPE`: AI model type - 'linear', 'polynomial', or 'decision_tree' (default: 'linear')

## Monitoring

### Health Check

The Streamlit app exposes a health endpoint:
```
GET /_stcore/health
```

Returns: `ok`

### Logs

View logs in real-time:
```bash
# Local development
streamlit run streamlit_app.py --server.runOnSave true

# Docker
docker logs -f container_id

# Systemd
sudo journalctl -u streamlit -f
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Use a different port
   streamlit run streamlit_app.py --server.port=8502
   ```

2. **Module not found**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

3. **Memory issues with large datasets**
   ```bash
   # Increase memory limit
   streamlit run streamlit_app.py --server.maxUploadSize=1000
   ```

### Performance Optimization

1. **Enable caching** - Already implemented with `@st.cache_resource`
2. **Optimize data loading** - Data is cached by default
3. **Use pagination** - For large datasets
4. **Compress images** - If using custom images

## Security

1. **Don't commit secrets** - Use `.streamlit/secrets.toml` (already in .gitignore)
2. **Enable XSRF protection** - Already enabled in config
3. **Use HTTPS** - Streamlit Cloud provides this automatically
4. **Validate inputs** - Already implemented

## Support

For issues or questions:
- GitHub Issues: https://github.com/yadavanujkumar/ai-driven-job-market-insights-dashboard/issues
- Documentation: https://docs.streamlit.io/

## Version

Current version: 2.1 (Streamlit Edition)
