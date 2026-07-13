
#imports
import pandas as pd

#Fetch mortgage rate data from FRED
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
mortgage

#Resampling weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (mortgage.groupby('year_month')['rate_30yr_fixed'].mean().reset_index())

#### Create matching year_month key on MLS datasets
#Sold dataset — key off CloseDate
sold = pd.read_csv("w2_sold_resid.csv")
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')

#Listings dataset — key off ListingContractDate
listing = pd.read_csv("w2_list_resid.csv")
listing['year_month'] = pd.to_datetime(listing['ListingContractDate']).dt.to_period('M')

#Merge
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listing_with_rates = listing.merge(mortgage_monthly, on='year_month', how='left')

#Validate merge - check for unmatched rows (rate should not be null)
print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(listing_with_rates['rate_30yr_fixed'].isnull().sum())

#Preview
print(sold_with_rates[['CloseDate', 'year_month', 'ClosePrice', 'rate_30yr_fixed']].head())


#Save enriched datasets as new CSVs
sold_with_rates.to_csv("w3_sold_fred.csv", index=False)
listing_with_rates.to_csv("w3_list_fred.csv", index=False)