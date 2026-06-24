# 🏡 MLS Housing Market Analytics Pipeline

## 📌 Overview

This project analyzes residential Multiple Listing Service (MLS) housing transaction data to generate market intelligence, competitive insights, and interactive business dashboards. Using **Python, Pandas, and Tableau**, the project transforms raw real estate transaction data into actionable insights on housing prices, inventory trends, market activity, and agent performance.

The project follows a complete data analytics workflow, including data aggregation, exploratory data analysis (EDA), data cleaning, feature engineering, economic data enrichment, outlier detection, and dashboard development.

---

## Objectives

- Combine and process monthly MLS listing and sold transaction datasets
- Clean and validate large-scale residential real estate data
- Enrich transaction records with mortgage rate data from FRED
- Engineer housing market performance metrics
- Detect and flag statistical outliers
- Analyze pricing, inventory, and market activity trends
- Evaluate agent and brokerage performance
- Develop interactive Tableau dashboards for market intelligence

---

## Data Notice: 
Due to MLS licensing and confidentiality restrictions, the underlying real estate transaction datasets are not included in this repository. This project showcases the complete analytics pipeline and methodology used to process and analyze MLS data rather than the proprietary data itself.

---

## 🗂️ Dataset

### 🏠 MLS Transaction Data
- Residential property listings
- Residential property sales
- January 2024 – Present
- Millions of transaction records

### 📈 Economic Data
- 30-Year Fixed Mortgage Rate (MORTGAGE30US)
- Source: Federal Reserve Economic Data (FRED)

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Tableau Public
- Jupyter Notebook
- FRED Economic Data API

---

## Project Workflow

### 1. Data Aggregation
- Combined monthly MLS listing and sold datasets
- Filtered records to residential properties only
- Created unified datasets for time-series analysis

### 2. Exploratory Data Analysis
- Analyzed dataset structure and completeness
- Identified missing values and data quality issues
- Examined distributions of:
  - Close Price
  - List Price
  - Living Area
  - Days on Market
  - Bedrooms and Bathrooms

### 3. Mortgage Rate Enrichment
- Retrieved mortgage rate data from FRED
- Resampled weekly rates into monthly averages
- Merged mortgage rates with MLS transactions

### 4. Data Cleaning
- Converted date fields to datetime format
- Validated transaction timelines
- Removed invalid records
- Flagged geographic inconsistencies
- Standardized numeric variables

### 5. Feature Engineering
Created key housing market metrics including:

| Metric | Formula |
|----------|----------|
| Price Ratio | ClosePrice / OriginalListPrice |
| Price per Sq Ft | ClosePrice / LivingArea |
| Days on Market | DaysOnMarket |
| Close-to-List Ratio | ClosePrice / OriginalListPrice |
| Listing-to-Contract Days | PurchaseContractDate − ListingContractDate |
| Contract-to-Close Days | CloseDate − PurchaseContractDate |

### 6. Outlier Detection
- Applied Interquartile Range (IQR) methodology
- Flagged extreme observations
- Created filtered datasets for market analysis

### 7. Market Analytics
Analyzed:
- Median home prices
- Housing inventory trends
- Sales volume
- Market velocity
- Pricing power
- Geographic market differences

### 8. Competitive Intelligence
Evaluated:
- Top-performing agents
- Top-performing brokerages
- Sales volume rankings
- Transaction unit rankings

### 9. Dashboard Development
Built Tableau dashboards covering:
- Monthly Median Close Price
- Average Days on Market
- Close-to-List Price Ratio
- New Listings
- Closed Sales
- Zip Code Heat Maps
- Agent Performance Rankings
- Brokerage Performance Rankings

---

## Key Skills Demonstrated

- Data Aggregation, Validation, and Cleaning
- Public API Integration (FRED)
- Exploratory Data Analysis (EDA)
- Datetime Processing & Join Key Creation
- Data Merging with External Economic Indicators
- Merge Verification & Null-Check Validation
- Feature Engineering
- Time Series Analysis
- Statistical Outlier Detection
- Dataset Reliability Improvement & Quality Assurance
- Data Visualization
- Business Intelligence
- Dashboard Development
- Real Estate Market Analytics

---

## (include repository structure here)

---

## 🔒 Data Availability & MLS Disclaimer

Note: The MLS datasets used for this project are not included in this repository.

Multiple Listing Service (MLS) data is not fully public because it is a privately owned and maintained database created by real estate brokerages and REALTOR® associations. These organizations invest significant resources to collect, verify, and maintain property listing information for use by licensed real estate professionals and their clients.

Because MLS data is proprietary, access is restricted to authorized users and participating organizations. The restrictions help:

- Protect proprietary business data
- Maintain competitive advantages for participating brokerages
- Safeguard client and property information
- Ensure compliance with MLS licensing agreements and usage policies

While this repository contains the complete analytics workflow—including data aggregation, cleaning, exploratory analysis, feature engineering, mortgage-rate enrichment, outlier detection, and Tableau dashboard development—the underlying MLS transaction data cannot be publicly distributed.
