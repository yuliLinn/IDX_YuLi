
# imports
import pandas as pd

# import all listing data
list1 = pd.read_csv("CRMLSListing202401.csv")
list2 = pd.read_csv("CRMLSListing202402.csv")
list3 = pd.read_csv("CRMLSListing202403.csv")
list4 = pd.read_csv("CRMLSListing202404.csv")
list5 = pd.read_csv("CRMLSListing202405.csv")
list6 = pd.read_csv("CRMLSListing202406.csv")
list7 = pd.read_csv("CRMLSListing202407.csv")
list8 = pd.read_csv("CRMLSListing202408.csv")
list9 = pd.read_csv("CRMLSListing202409.csv")
list10 = pd.read_csv("CRMLSListing202410.csv")
list11 = pd.read_csv("CRMLSListing202411.csv")
list12 = pd.read_csv("CRMLSListing202412.csv")
list13 = pd.read_csv("CRMLSListing202501.csv")
list14 = pd.read_csv("CRMLSListing202502.csv")
list15 = pd.read_csv("CRMLSListing202503.csv")
list16 = pd.read_csv("CRMLSListing202504.csv")
list17 = pd.read_csv("CRMLSListing202505.csv")
list18 = pd.read_csv("CRMLSListing202506.csv")
list19 = pd.read_csv("CRMLSListing202507.csv")
list20 = pd.read_csv("CRMLSListing202508.csv")
list21 = pd.read_csv("CRMLSListing202509.csv")
list22 = pd.read_csv("CRMLSListing202510.csv")
list23 = pd.read_csv("CRMLSListing202511.csv")
list24 = pd.read_csv("CRMLSListing202512.csv")
list25 = pd.read_csv("CRMLSListing202601.csv")
list26 = pd.read_csv("CRMLSListing202602.csv")
list27 = pd.read_csv("CRMLSListing202603.csv")
list28 = pd.read_csv("CRMLSListing202604.csv")
list29 = pd.read_csv("CRMLSListing202605.csv", encoding="cp1252")
list30 = pd.read_csv("CRMLSListing202606.csv", encoding="cp1252")

#concatenate listing data
list = pd.concat([globals()[f'list{i}'] for i in range(1, 31)], ignore_index=True)

#validate number of observations before and after concatenation for listing
rows_list_pre = sum(len(globals()[f'list{i}']) for i in range(1, 31))
rows_list_post = len(list)
print(f"Before: {rows_list_pre:,} | After: {rows_list_post:,}")


# apply residential filter to listing data and save as new CSV file
list_resid = list[list["PropertyType"] == "Residential"]
print(f"(Listing) Before: {len(list):,} | After: {len(list_resid):,}")



# import all sold data
sold1 = pd.read_csv("CRMLSSold202401_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold2 = pd.read_csv("CRMLSSold202401.csv")
sold3 = pd.read_csv("CRMLSSold202402.csv")
sold4 = pd.read_csv("CRMLSSold202403_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold5 = pd.read_csv("CRMLSSold202403.csv")
sold6 = pd.read_csv("CRMLSSold202404_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold7 = pd.read_csv("CRMLSSold202404.csv")
sold8 = pd.read_csv("CRMLSSold202405_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold9 = pd.read_csv("CRMLSSold202406_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold10 = pd.read_csv("CRMLSSold202407_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold11 = pd.read_csv("CRMLSSold202408.csv")
sold12 = pd.read_csv("CRMLSSold202409.csv")
sold13 = pd.read_csv("CRMLSSold202410.csv")
sold14 = pd.read_csv("CRMLSSold202411.csv")
sold15 = pd.read_csv("CRMLSSold202412.csv")
sold16 = pd.read_csv("CRMLSSold202501_filled.csv").drop(columns = ["latfilled", "lonfilled"])
sold17 = pd.read_csv("CRMLSSold202502.csv")
sold18 = pd.read_csv("CRMLSSold202503.csv")
sold19 = pd.read_csv("CRMLSSold202504.csv")
sold20 = pd.read_csv("CRMLSSold202505.csv")
sold21 = pd.read_csv("CRMLSSold202506.csv")
sold22 = pd.read_csv("CRMLSSold202507.csv")
sold23 = pd.read_csv("CRMLSSold202508.csv")
sold24 = pd.read_csv("CRMLSSold202509.csv")
sold25 = pd.read_csv("CRMLSSold202510.csv")
sold26 = pd.read_csv("CRMLSSold202511.csv")
sold27 = pd.read_csv("CRMLSSold202512.csv")
sold28 = pd.read_csv("CRMLSSold202601.csv")
sold29 = pd.read_csv("CRMLSSold202602.csv")
sold30 = pd.read_csv("CRMLSSold202603.csv")
sold31 = pd.read_csv("CRMLSSold202604.csv")
sold32 = pd.read_csv("CRMLSSold202605.csv", encoding="cp1252")
sold33 = pd.read_csv("CRMLSSold202606.csv", encoding="cp1252")

# concatenate all sold data
sold = pd.concat([globals()[f'sold{i}'] for i in range(1, 34)], ignore_index=True)

#validate number of observations before and after concatenation for sold
rows_sold_pre = sum(len(globals()[f'sold{i}']) for i in range(1, 34))
rows_sold_post = len(sold)
print(f"Before: {rows_sold_pre:,} | After: {rows_sold_post:,}")

# apply residential filter to listing data and save as new CSV file
sold_resid = sold[sold["PropertyType"] == "Residential"]
print(f"(Sold) Before:{len(sold):,} | After: {len(sold_resid):,}")



# save filtered as csv files
list_resid.to_csv("week1_list_resid.csv", index=False)
sold_resid.to_csv("week1_sold_resid.csv", index=False)