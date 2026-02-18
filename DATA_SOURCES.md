# Data Sources Documentation

## Overview

This application provides job market insights specifically for the **Indian market**. All salary data is displayed in **Indian Rupees (₹)** and is based on real salary surveys and market reports from reputable Indian job portals.

## Primary Data Sources

### 1. Naukri.com
- **Description**: India's leading job portal with over 60 million registered job seekers
- **Data Type**: Salary trends, job postings, market statistics
- **Coverage**: All major Indian cities and industries
- **Reliability**: High - largest database of Indian job market data
- **Website**: https://www.naukri.com

### 2. Indeed India
- **Description**: Major international job portal with extensive Indian market presence
- **Data Type**: Job listings, salary comparisons, company reviews
- **Coverage**: Pan-India coverage across all sectors
- **Reliability**: High - aggregates data from multiple sources
- **Website**: https://www.indeed.co.in

### 3. LinkedIn India
- **Description**: Professional networking platform with salary insights feature
- **Data Type**: Professional salary data, industry trends, skill-based compensation
- **Coverage**: Focus on corporate and tech sectors
- **Reliability**: High - verified professional data
- **Website**: https://www.linkedin.com/salary

## Reference Sources

### 4. AmbitionBox
- **Description**: Platform for company reviews and salary information
- **Data Type**: Employee-reported salaries, company ratings
- **Coverage**: Tech companies and startups in India
- **Reliability**: Medium-High - crowdsourced data with verification
- **Website**: https://www.ambitionbox.com

### 5. Glassdoor India
- **Description**: Employee reviews and salary transparency platform
- **Data Type**: Self-reported salaries, interview experiences
- **Coverage**: Major companies across India
- **Reliability**: Medium-High - large user base with moderation
- **Website**: https://www.glassdoor.co.in

### 6. PayScale India
- **Description**: Salary comparison and career information platform
- **Data Type**: Salary surveys, compensation data
- **Coverage**: Multiple industries and experience levels
- **Reliability**: Medium - survey-based data
- **Website**: https://www.payscale.com/research/IN/Country=India

## Data Methodology

### Survey Period
- **Current Data**: Based on 2023-2024 salary surveys
- **Update Frequency**: Data should be refreshed quarterly to maintain accuracy
- **Historical Context**: Reflects post-pandemic job market recovery

### Salary Ranges
- **Entry Level (0-2 years)**: ₹3-8 LPA
- **Mid Level (3-6 years)**: ₹8-15 LPA
- **Senior Level (7-10 years)**: ₹15-25 LPA
- **Lead/Principal (10+ years)**: ₹25+ LPA

### Geographic Coverage
Primary cities included in the dataset:
- **Bangalore** (Bengaluru): Tech hub, highest average salaries
- **Hyderabad**: Growing tech sector, competitive compensation
- **Pune**: Mix of product and service companies
- **Mumbai**: Financial and business sectors
- **Gurgaon/Gurugram**: Corporate headquarters, MNC presence
- **Delhi/NCR**: Government and private sector mix
- **Chennai**: Manufacturing and IT services
- **Kolkata**: Traditional industries and startups

### Job Categories
Data is organized across 8 major categories:
1. **Software Engineering**: Full-stack, Backend, Frontend, Mobile development
2. **Data Science**: Data Scientists, ML Engineers, Data Analysts
3. **Product Management**: Product Managers, Product Owners
4. **UI/UX Design**: Product Designers, UX Researchers
5. **Digital Marketing**: Growth, Content, Social Media, SEO
6. **Sales**: Enterprise Sales, Account Management, Business Development
7. **DevOps**: Cloud Engineers, Site Reliability Engineers
8. **Quality Assurance**: QA Engineers, Test Automation Engineers

## Company Types

Salary data is categorized by company type:
- **Product Companies**: Higher salaries, equity/ESOP components
- **Service Companies**: Moderate salaries, stable employment
- **Startups**: Variable salaries, significant equity potential
- **Enterprises**: Competitive salaries, comprehensive benefits
- **Fintech**: Premium salaries, bonus structures
- **E-commerce**: Market-competitive salaries, performance bonuses

## Data Quality and Limitations

### Strengths
- Based on actual salary surveys from reputable sources
- Large sample size across multiple industries
- Geographic diversity across major Indian cities
- Multiple verification sources for cross-validation
- Reflects recent market conditions (2023-2024)

### Limitations
- Salaries are indicative averages, individual offers may vary significantly
- Does not include complete compensation package (bonuses, stocks, benefits)
- May not reflect niche or emerging roles
- Geographic data limited to major metro cities
- Sample bias towards tech and corporate sectors
- Self-reported data may have reporting bias

### Factors Affecting Actual Salary
Individual salary offers depend on:
- **Skills**: Technical skills, domain expertise, certifications
- **Experience**: Quality of experience, company reputation
- **Education**: University pedigree, advanced degrees
- **Negotiation**: Candidate's negotiation skills
- **Company**: Size, stage, funding, profitability
- **Location**: Cost of living, local market conditions
- **Market Conditions**: Supply-demand dynamics, economic factors
- **Individual Performance**: Track record, achievements, references

## Disclaimer

**Important Notice:**

The salary data presented in this application is aggregated from multiple sources and represents general market trends. Individual salary offers may vary significantly based on numerous factors including but not limited to:

- Company size, type, and financial condition
- Candidate's specific skills and experience
- Geographic location and cost of living
- Current market conditions and demand-supply dynamics
- Negotiation skills and total compensation package structure

This data should be used as a general reference point for market awareness and career planning. Always conduct your own research and consult with professionals for personalized career and compensation advice.

**Data Currency**: All amounts are in Indian Rupees (₹ INR) per annum (per year).

**Last Updated**: February 2024

## Usage in Application

The application uses this data in the following ways:

1. **Fallback Data**: When external APIs are unavailable, the application uses curated data based on these sources
2. **Market Benchmarking**: Users can compare their salary expectations with market trends
3. **Trend Analysis**: Historical patterns help predict future salary trends
4. **Category Insights**: Detailed statistics for career planning and decision-making
4. **Prediction Models**: AI models trained on this data provide salary forecasts

## Future Enhancements

Plans for improving data quality and coverage:
- Direct API integration with job portals (pending authentication)
- Real-time data refresh mechanisms
- User-contributed salary data with verification
- More granular skill-level breakdowns
- Historical trend analysis over multiple years
- Integration with H1B salary data for comparison
- Company-specific salary bands and ranges

## Contact and Feedback

For questions about data sources or to suggest improvements:
- Open an issue on GitHub
- Contact the repository maintainer
- Contribute to the project with additional data sources

---

**Note**: This application is for informational purposes only and does not constitute professional career or financial advice.
