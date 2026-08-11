
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Datasets
df_sold = pd.read_csv("w6_sold_KeyMetrics.csv", low_memory=False)
df_listing = pd.read_csv("w6_listing_KeyMetrics.csv", low_memory=False)

##Flagging low and high outliers
#Columns to detect for outliers
cols = ["ClosePrice", "price_per_sqft", "DaysOnMarket", "LivingArea"]

#Flagging low and high outliers
for df in [df_sold, df_listing]:
    for col in cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR

        flag_col = f"flag_{col}_outlier"

        df[flag_col] = np.nan
        df.loc[df[col] < lower, flag_col] = "low"
        df.loc[df[col] > upper, flag_col] = "high"

#Save outlier flagged datasets as new CSVs
df_sold.to_csv("w7_sold_flagged.csv")
df_listing.to_csv("w7_list_flagged.csv")

##Remove rows with outliers in ["ClosePrice", "price_per_sqft", "DaysOnMarket", "LivingArea"]
#Sold
flag_col = ["flag_ClosePrice_outlier", "flag_price_per_sqft_outlier", "flag_DaysOnMarket_outlier", "flag_LivingArea_outlier"]
sold_remove = df_sold[~df_sold[flag_col].isin(["low", "high"]).any(axis=1)].reset_index(drop=True)

#Listing
listing_remove = df_listing[~df_listing[flag_col].isin(["low", "high"]).any(axis=1)].reset_index(drop=True)

#Remove flagged columns
sold_remove = sold_remove.drop(columns=df_sold.filter(like="flag_").columns)
listing_remove = listing_remove.drop(columns=df_listing.filter(like="flag_").columns)

#Save outlier removed version as new CSVs
sold_remove.to_csv("w7_sold_removed.csv")
listing_remove.to_csv("w7_listing_removed.csv")


##Comparing data before and after outlier removal
#Dataset size
print("Before")
print(f"Sold: {len(df_sold):,}")
print(f"Listing {len(df_listing):,}")
print()

print("After")
print(f"Sold: {len(sold_remove):,}")
print(f"Listing {len(listing_remove):,}")

#Median values
print("Before")
print(f"Sold: {df_sold["ClosePrice"].quantile(0.5):,}")
print(f"Listing {df_listing["ClosePrice"].quantile(0.5):,}")
print()

print("After")
print(f"Sold: {sold_remove["ClosePrice"].quantile(0.5):,}")
print(f"Listing {listing_remove["ClosePrice"].quantile(0.5):,}")

##Distribution of ClosePrice for sold data
#Boxplot with outliers
outlier = plt.boxplot(df_sold["ClosePrice"].dropna(), vert=False)
outlier = plt.title("ClosePrice with outliers")
outlier = plt.xlabel("in billion $")
outlier

#Boxplot without outliers
remove = plt.boxplot(sold_remove["ClosePrice"].dropna(), vert=False)
remove = plt.title("ClosePrice without outliers")
remove = plt.xlabel("in million $")
remove
