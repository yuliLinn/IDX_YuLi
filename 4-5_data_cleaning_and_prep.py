
#imports
import pandas as pd

#Import full data
sold_with_rates = pd.read_csv("w3_sold_fred.csv")
listing_with_rates = pd.read_csv("w3_list_fred.csv")

#Inspecting format of date-related columns
date_columns = ["CloseDate", "PurchaseContractDate", "ListingContractDate", "ContractStatusChangeDate"]

print(f"Sold:\n{sold_with_rates[date_columns].dtypes}")
print()
print(f"Listing:\n{listing_with_rates.dtypes[date_columns]}")

#Convert date fields to datetime format
sold_with_rates[date_columns] = sold_with_rates[date_columns].apply(pd.to_datetime)
listing_with_rates[date_columns] = listing_with_rates[date_columns].apply(pd.to_datetime)

print(f"Sold:\n{sold_with_rates[date_columns].dtypes}")
print()
print(f"Listing:\n{listing_with_rates.dtypes[date_columns]}")

##Date consistency checks
#Validate the logical order of date fields: ListingContractDate should precede PurchaseContractDate, which should precede CloseDate
sold_with_rates["listing_after_close_flag"] = (sold_with_rates["ListingContractDate"] > sold_with_rates["CloseDate"])

sold_with_rates["purchase_after_close_flag"] = (sold_with_rates["PurchaseContractDate"] > sold_with_rates["CloseDate"])

sold_with_rates["negative_timeline_flag"] = (
    (sold_with_rates["ListingContractDate"] > sold_with_rates["PurchaseContractDate"]) |
    (sold_with_rates["PurchaseContractDate"] > sold_with_rates["CloseDate"]) |
    (sold_with_rates["ListingContractDate"] > sold_with_rates["CloseDate"])
)

#Flag columns that violate rules as True
flag_columns = [
    "listing_after_close_flag",
    "purchase_after_close_flag",
    "negative_timeline_flag"
]

print("Sold:")
print(sold_with_rates[flag_columns].sum())

#Remove rows that violate logical time order
rows_before = len(sold_with_rates)

sold_timely = sold_with_rates[~sold_with_rates["negative_timeline_flag"]]
rows_after = len(sold_timely)

print("Sold (time cleaning):")
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")

#Repeat date check for listing data
listing_with_rates["listing_after_close_flag"] = (listing_with_rates["ListingContractDate"] > listing_with_rates["CloseDate"])

listing_with_rates["purchase_after_close_flag"] = (listing_with_rates["PurchaseContractDate"] > listing_with_rates["CloseDate"])

listing_with_rates["negative_timeline_flag"] = (
    (listing_with_rates["ListingContractDate"] > listing_with_rates["PurchaseContractDate"]) |
    (listing_with_rates["PurchaseContractDate"] > listing_with_rates["CloseDate"]) |
    (listing_with_rates["ListingContractDate"] > listing_with_rates["CloseDate"])
)

print("Listing (time cleaning):")
print(listing_with_rates[flag_columns].sum())

rows_before = len(listing_with_rates)

list_timely = listing_with_rates[~listing_with_rates["negative_timeline_flag"]]
rows_after = len(list_timely)

print()
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")

##Geographic data checks
#Flag records with missing coordinates
sold_timely["missing_cords"] = (sold_timely["Latitude"] == 0) | sold_timely["Longitude"] == 0

#Flag implausible or out-of_state coordinates 
#Latitude: Between 32.5343 and 42.0095
#Longitude: Between -124.4323 and -114.1312
sold_timely["invalid_cords"] = (
    (sold_timely["Latitude"] < 32.5343) |
    (sold_timely["Latitude"] > 42.0095) |
    (sold_timely["Longitude"] < -124.4323) |
    (sold_timely["Longitude"] > -114.1312)
)

missing = len(sold_timely[(sold_timely["missing_cords"] == True)])
invalid = len(sold_timely[(sold_timely["invalid_cords"] == True)])

print("Sold:")
print(f"Missing Coordinates: {missing:,}")
print(f"Invalid Coordinates: {invalid:,}")
print(f"Total: {(missing + invalid):,}")

#Remove fields with missing or invalid coordinates for accurate Califlorina-only analysis
sold_geo = sold_timely[~(sold_timely["invalid_cords"] | sold_timely["missing_cords"])]

rows_before = len(sold_timely)
rows_after = len(sold_geo)

print("Sold (coordinate cleaning):")
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")

#Repeat for geographic check for listing data
list_timely["missing_cords"] = (list_timely["Latitude"] == 0) | list_timely["Longitude"] == 0

list_timely["invalid_cords"] = (
    (list_timely["Latitude"] < 32.5343) |
    (list_timely["Latitude"] > 42.0095) |
    (list_timely["Longitude"] < -124.4323) |
    (list_timely["Longitude"] > -114.1312)
)

missing = len(list_timely[(list_timely["missing_cords"] == True)])
invalid = len(list_timely[(list_timely["invalid_cords"] == True)])

print()
print("Listing (coordinate cleaning):")
print(f"Missing Coordinates: {missing:,}")
print(f"Invalid Coordinates: {invalid:,}")
print(f"Total: {(missing + invalid):,}")

list_geo = list_timely[~(list_timely["invalid_cords"] | list_timely["missing_cords"])]

rows_before = len(list_timely)
rows_after = len(list_geo)

print()
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")

#Remove invalid numeric values (no negative ClosePrice, LivingArea, DaysOnMarket, Bedrooms, or Bathrooms)
sold_clean = sold_geo[
    (sold_geo["ClosePrice"] > 0) &
    (sold_geo["LivingArea"] > 0) &
    (sold_geo["DaysOnMarket"] >= 0) &
    (sold_geo["BedroomsTotal"] >= 0) &
    (sold_geo["BathroomsTotalInteger"] >= 0)
]

rows_before = len(sold_geo)
rows_after = len(sold_clean)

print("Sold (invalids):")
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")

#Repeat for listing data
list_clean = list_geo[
    (list_geo["LivingArea"] > 0) &
    (list_geo["DaysOnMarket"] >= 0) &
    (list_geo["BedroomsTotal"] >= 0) &
    (list_geo["BathroomsTotalInteger"] >= 0)
]

rows_before = len(list_geo)
rows_after = len(list_clean)

print("Listing (invalids):")
print(f"Rows before: {rows_before:,}")
print(f"Rows after: {rows_after:,}")
print(f"Rows removed: {rows_before - rows_after:,}")


##Final sweep to remove unnecessart columns
#Removing unnecessary columns for sold and listing data
sold_clean = sold_clean.drop(columns=["BuyerAgencyCompensationType"])
list_clean = list_clean.drop(columns=["BuyerAgencyCompensationType"])

#Remove flagging columns
sold_clean = sold_clean.drop(columns=["listing_after_close_flag", "purchase_after_close_flag", "negative_timeline_flag", "missing_cords", "invalid_cords"])
list_clean = list_clean.drop(columns=["listing_after_close_flag", "purchase_after_close_flag", "negative_timeline_flag", "missing_cords", "invalid_cords"])

#Final row count before and after cleaning
sold_before = len(sold_with_rates)
print("Final row count before and after cleaning")

print()
print("Sold:")
print(f"Rows before: {len(sold_with_rates):,}")
print(f"Rows after: {len(sold_clean):,}")
print(f"Rows removed: {len(sold_with_rates) - len(sold_clean):,}")

print()
print("Listing:")
print(f"Rows before: {len(listing_with_rates):,}")
print(f"Rows after: {len(list_clean):,}")
print(f"Rows removed: {len(listing_with_rates) - len(list_clean):,}")


#Save cleaned datasets as new CSVs
sold_clean.to_csv("w4_sold_clean.csv", index=False)
list_clean.to_csv("w4_listing_clean.csv", index=False)