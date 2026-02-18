import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.services.job_service import JobService
from src.utils.logger import setup_logger

# Configure page
st.set_page_config(
    page_title="AI Job Market Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize logger and service
logger = setup_logger(__name__)

@st.cache_resource
def get_job_service():
    """Initialize and cache the job service."""
    return JobService()

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    h1 {
        color: #8B5CF6;
    }
    .css-1d391kg {
        padding-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    """Main Streamlit application."""
    
    # Header
    st.title("📊 AI-Driven Job Market Insights Dashboard")
    st.markdown("---")
    
    # Initialize service
    job_service = get_job_service()
    
    # Sidebar
    st.sidebar.title("🔧 Settings")
    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Trends Analysis", "Salary Prediction", "About"]
    )
    
    # Cache management
    if st.sidebar.button("🔄 Clear Cache"):
        job_service.clear_cache()
        st.cache_data.clear()
        st.sidebar.success("Cache cleared successfully!")
    
    # Main content based on selected page
    if page == "Dashboard":
        show_dashboard(job_service)
    elif page == "Trends Analysis":
        show_trends_analysis(job_service)
    elif page == "Salary Prediction":
        show_prediction(job_service)
    else:
        show_about()

def show_dashboard(job_service):
    """Display main dashboard with statistics and visualizations."""
    st.header("📈 Market Overview")
    
    try:
        # Get statistics
        with st.spinner("Loading market data..."):
            stats = job_service.get_statistics()
            trends = job_service.get_job_trends()
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Jobs",
                value=f"{stats['total_jobs']:,}",
                delta=None
            )
        
        with col2:
            st.metric(
                label="Categories",
                value=stats['total_categories'],
                delta=None
            )
        
        with col3:
            st.metric(
                label="Avg Salary",
                value=f"${stats['overall_average_salary']:,.0f}",
                delta=None
            )
        
        with col4:
            salary_range = stats['salary_range']
            st.metric(
                label="Salary Range",
                value=f"${salary_range['min']:,.0f} - ${salary_range['max']:,.0f}",
                delta=None
            )
        
        st.markdown("---")
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Average Salary by Category")
            
            # Prepare data for bar chart
            categories = []
            avg_salaries = []
            for category, data in trends.items():
                categories.append(category)
                avg_salaries.append(data['average_salary'])
            
            fig = px.bar(
                x=categories,
                y=avg_salaries,
                labels={'x': 'Job Category', 'y': 'Average Salary ($)'},
                color=avg_salaries,
                color_continuous_scale='Viridis'
            )
            fig.update_layout(
                showlegend=False,
                height=400,
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Job Distribution")
            
            # Prepare data for pie chart
            job_counts = [data['job_count'] for data in trends.values()]
            
            fig = px.pie(
                values=job_counts,
                names=categories,
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Detailed statistics table
        st.markdown("---")
        st.subheader("📋 Detailed Category Statistics")
        
        # Create DataFrame for detailed view
        details_data = []
        for category, data in trends.items():
            details_data.append({
                'Category': category,
                'Count': data['job_count'],
                'Avg Salary': f"${data['average_salary']:,.0f}",
                'Median': f"${data['median_salary']:,.0f}",
                'Min': f"${data['min_salary']:,.0f}",
                'Max': f"${data['max_salary']:,.0f}",
                'Std Dev': f"${data['std_deviation']:,.0f}"
            })
        
        df = pd.DataFrame(details_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
    except Exception as e:
        st.error(f"Error loading dashboard data: {str(e)}")
        logger.error(f"Dashboard error: {str(e)}")

def show_trends_analysis(job_service):
    """Display detailed trends analysis."""
    st.header("📊 Trends Analysis")
    
    try:
        with st.spinner("Analyzing job market trends..."):
            trends = job_service.get_job_trends()
        
        # Category selector
        selected_category = st.selectbox(
            "Select Job Category",
            options=list(trends.keys())
        )
        
        if selected_category:
            category_data = trends[selected_category]
            
            # Display category metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Jobs Available", category_data['job_count'])
            with col2:
                st.metric("Average Salary", f"${category_data['average_salary']:,.0f}")
            with col3:
                st.metric("Median Salary", f"${category_data['median_salary']:,.0f}")
            
            st.markdown("---")
            
            # Salary statistics visualization
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Salary Statistics")
                
                # Create box plot data
                fig = go.Figure()
                fig.add_trace(go.Box(
                    y=[
                        category_data['min_salary'],
                        category_data['average_salary'] - category_data['std_deviation'],
                        category_data['median_salary'],
                        category_data['average_salary'] + category_data['std_deviation'],
                        category_data['max_salary']
                    ],
                    name=selected_category,
                    marker_color='indianred'
                ))
                fig.update_layout(
                    yaxis_title="Salary ($)",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Salary Range")
                
                # Create gauge chart for salary position
                salary_range = category_data['max_salary'] - category_data['min_salary']
                avg_position = category_data['average_salary'] - category_data['min_salary']
                
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=category_data['average_salary'],
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Average Salary"},
                    delta={'reference': category_data['median_salary']},
                    gauge={
                        'axis': {'range': [category_data['min_salary'], category_data['max_salary']]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [category_data['min_salary'], category_data['median_salary']], 'color': "lightgray"},
                            {'range': [category_data['median_salary'], category_data['max_salary']], 'color': "gray"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': category_data['average_salary']
                        }
                    }
                ))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
            
            # Detailed information
            st.markdown("---")
            st.subheader("📊 Statistical Summary")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Minimum Salary:** ${category_data['min_salary']:,.0f}")
                st.write(f"**Maximum Salary:** ${category_data['max_salary']:,.0f}")
                st.write(f"**Salary Range:** ${category_data['max_salary'] - category_data['min_salary']:,.0f}")
            
            with col2:
                st.write(f"**Average Salary:** ${category_data['average_salary']:,.0f}")
                st.write(f"**Median Salary:** ${category_data['median_salary']:,.0f}")
                st.write(f"**Standard Deviation:** ${category_data['std_deviation']:,.0f}")
            
    except Exception as e:
        st.error(f"Error loading trends data: {str(e)}")
        logger.error(f"Trends analysis error: {str(e)}")

def show_prediction(job_service):
    """Display salary prediction interface."""
    st.header("🔮 Salary Prediction")
    st.write("Predict future salary trends using AI/ML models")
    
    # Model selection
    model_type = st.selectbox(
        "Select Prediction Model",
        ["linear", "polynomial", "decision_tree"],
        help="Choose the machine learning model for prediction"
    )
    
    st.markdown("---")
    
    # Input section
    st.subheader("📥 Input Historical Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        years_input = st.text_input(
            "Historical Years (comma-separated)",
            value="2020,2021,2022,2023",
            help="Enter years for historical data"
        )
        
    with col2:
        salaries_input = st.text_input(
            "Historical Salaries (comma-separated)",
            value="95000,105000,115000,125000",
            help="Enter corresponding salary values"
        )
    
    future_years_input = st.text_input(
        "Future Years to Predict (comma-separated)",
        value="2024,2025,2026",
        help="Enter years for which to predict salaries"
    )
    
    if st.button("🚀 Predict Future Trends", type="primary"):
        try:
            # Parse inputs
            years = [int(y.strip()) for y in years_input.split(',')]
            salaries = [float(s.strip()) for s in salaries_input.split(',')]
            future_years = [int(y.strip()) for y in future_years_input.split(',')]
            
            # Validate input lengths
            if len(years) != len(salaries):
                st.error("Number of years and salaries must match!")
                return
            
            if len(years) < 2:
                st.error("Please provide at least 2 historical data points!")
                return
            
            # Prepare request data
            prediction_data = {
                'years': years,
                'salaries': salaries,
                'future_years': future_years
            }
            
            # Make prediction
            with st.spinner("Making predictions..."):
                result = job_service.predict_job_trends(prediction_data)
            
            # Display results
            st.success("✅ Prediction completed successfully!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Model Used", result['model_type'].replace('_', ' ').title())
                st.metric("Confidence Score", f"{result['confidence_score']:.2%}")
            
            with col2:
                predictions = result['predictions']
                avg_predicted = sum(predictions) / len(predictions)
                st.metric("Average Predicted Salary", f"${avg_predicted:,.0f}")
            
            # Visualization
            st.markdown("---")
            st.subheader("📈 Prediction Visualization")
            
            # Combine historical and predicted data
            all_years = years + future_years
            all_salaries = salaries + predictions
            
            # Create DataFrame
            df_historical = pd.DataFrame({
                'Year': years,
                'Salary': salaries,
                'Type': 'Historical'
            })
            
            df_predicted = pd.DataFrame({
                'Year': future_years,
                'Salary': predictions,
                'Type': 'Predicted'
            })
            
            df_combined = pd.concat([df_historical, df_predicted])
            
            # Create line chart
            fig = px.line(
                df_combined,
                x='Year',
                y='Salary',
                color='Type',
                markers=True,
                title="Salary Trend: Historical vs Predicted"
            )
            fig.update_layout(
                height=500,
                xaxis_title="Year",
                yaxis_title="Salary ($)",
                hovermode='x unified'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed predictions table
            st.subheader("📋 Detailed Predictions")
            predictions_df = pd.DataFrame({
                'Year': future_years,
                'Predicted Salary': [f"${p:,.0f}" for p in predictions]
            })
            st.dataframe(predictions_df, use_container_width=True, hide_index=True)
            
        except ValueError as e:
            st.error(f"Invalid input format: {str(e)}")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
            logger.error(f"Prediction error: {str(e)}")

def show_about():
    """Display about page."""
    st.header("ℹ️ About This Dashboard")
    
    st.markdown("""
    ### AI-Driven Job Market Insights Dashboard
    
    This interactive dashboard provides comprehensive insights into the job market using AI and machine learning.
    
    #### 🎯 Features
    
    - **Real-time Data Analysis**: Get up-to-date job market statistics and trends
    - **Interactive Visualizations**: Explore data through intuitive charts and graphs
    - **AI-Powered Predictions**: Forecast future salary trends using machine learning
    - **Multiple ML Models**: Choose from Linear Regression, Polynomial Regression, or Decision Tree models
    - **Comprehensive Statistics**: View detailed statistics for each job category
    
    #### 🔧 Technologies
    
    - **Streamlit**: Interactive web application framework
    - **Scikit-learn**: Machine learning models
    - **Plotly**: Interactive visualizations
    - **Pandas**: Data manipulation and analysis
    - **NumPy**: Numerical computing
    
    #### 📊 Data Categories
    
    The dashboard analyzes job market data across multiple categories including:
    - Engineering
    - Data Science
    - Product Management
    - Design
    - Marketing
    - Sales
    
    #### 🚀 How to Use
    
    1. **Dashboard**: View overall market statistics and trends
    2. **Trends Analysis**: Dive deep into specific job categories
    3. **Salary Prediction**: Forecast future salary trends with AI models
    
    #### 📝 Notes
    
    - Data is cached for performance optimization
    - Use the "Clear Cache" button to refresh data
    - Predictions are based on historical trends and may not reflect actual future values
    
    ---
    
    **Version**: 2.1 (Streamlit Edition)
    
    **Repository**: [GitHub](https://github.com/yadavanujkumar/ai-driven-job-market-insights-dashboard)
    """)

if __name__ == "__main__":
    main()
