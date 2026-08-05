
import pandas as pd
#To display key metrics as dataframe
from IPython.display import display

df_sold = pd.read_csv("w4_sold_clean.csv", low_memory=False)
df_listing = pd.read_csv("w4_listing_clean.csv", low_memory=False)

#Convert date fields to datetime format
sold_with_rates = pd.read_csv("w3_sold_fred.csv")
listing_with_rates = pd.read_csv("w3_list_fred.csv")

date_columns = ["CloseDate", "PurchaseContractDate", "ListingContractDate", "ContractStatusChangeDate"]

df_sold[date_columns] = sold_with_rates[date_columns].apply(pd.to_datetime)
df_listing[date_columns] = listing_with_rates[date_columns].apply(pd.to_datetime)

print(f"Sold:\n{df_sold[date_columns].dtypes}")
print()
print(f"Listing:\n{df_listing.dtypes[date_columns]}")

#Creating key metrics
dfs = [df_sold, df_listing]

for df in dfs:
    #Price Ratio
    df["price_ratio"] = df["ClosePrice"] / df["OriginalListPrice"]

    #Price Per Sq Ft
    df["price_per_sqft"] = df["ClosePrice"] / df["LivingArea"]

    #Close to Original List Ratio
    df["close_to_original_ratio"] = df["ClosePrice"]/df["OriginalListPrice"]

    #Listing to Contract Days
    df["list_to_contract_days"] = (df["PurchaseContractDate"] - df["ListingContractDate"]).dt.days

    #Contract to Close Days
    df["contract_to_close_days"] = (df["CloseDate"] - df["PurchaseContractDate"]).dt.days
    
#Display sample of key metrics
key_metrics = ["price_ratio", "price_per_sqft", "DaysOnMarket", "CloseDate", "close_to_original_ratio", "list_to_contract_days", "contract_to_close_days"]

#Sold sample output table
sold_key_metrics = df_sold[key_metrics]
print("Sold:")
display(sold_key_metrics.head())
print()

#Listing sample output table
listing_key_metrics = df_listing[key_metrics]
print("Listing")
display(listing_key_metrics.head())


##Segmented Analysis
#Function to group analysis by key functions
def segment_analysis(df, segment_col):
    return (
        df.groupby(segment_col).agg(
            count=("ClosePrice", "count"),
            avg_price=("ClosePrice", "mean"),
            median_price=("ClosePrice", "median"),
            avg_price_ratio=("price_ratio", "mean"),
            avg_price_per_sqft=("price_per_sqft", "mean"),
            avg_list_to_contract_days=("list_to_contract_days", "mean"),
            avg_contract_to_close_days=("contract_to_close_days", "mean")
        )
        .sort_values("count", ascending=False)
    )

# Apply to sold and listing data
datasets = {"sold": df_sold, "listing": df_listing}

segments = [
    "PropertyType",
    "PropertySubType",
    "CountyOrParish",
    "MLSAreaMajor",
    "ListOfficeName",
    "BuyerOfficeName"
]

# Create a summary DataFrame for each segment
#EX. sold/listing_propertytype_analysis
for name, df in datasets.items():
    for segment in segments:
        if segment in df.columns:
            globals()[f"{name}_{segment.lower()}_analysis"] = segment_analysis(df, segment)



#Sample summary table of offices (competitve intelligence)
sold_listofficename_analysis.head(10)

#Sample summary by PropertyType
listing_propertytype_analysis.head(10)
