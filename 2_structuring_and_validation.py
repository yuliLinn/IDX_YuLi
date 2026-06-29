
# imports
import pandas as pd

# Datasets
sold = pd.read_csv("w1_sold_resid.csv")
list = pd.read_csv("w1_list_resid.csv")

# Inspecting structure
sold.columns

# Data snapshot
pd.set_option('display.max_columns', None)
sold.head()

sold["PropertyType"].value_counts()

#### Focusing on residential properties, including:
    # - "Residential": standard homes intended for owner-occupany
    # - "ResidentialLease": residential properties offered for rent
    # - "ResidentialIncome": multi-unit residential properties purchased primarily for rental income
# Chose to focus on traditional residential home sales and excluded "ManufacturedInPark" homes (mobile homes) located in mobile home parks 
# Differ in terms of ownership structure, financing, depreciation, and market dyanmics.
# Since  mix mobil/manufactured homes and traditional site-built residential represent fundamentally different asset classes analyzing them together can severely skew metrics.
# After filtering, the new dataset for sales of traditional, residential homes decreases from 681599 to 632055.
sold_resid = sold[sold["PropertyType"].isin(["Residential", "ResidentialLease", "ResidentialIncome"])]

# Validating completness for sold data
null_report_sold = pd.DataFrame({
    "Null Count": sold_resid.isnull().sum(),
    "Null %": (sold_resid.isnull().sum() / len(sold_resid) * 100).round(2)
})
null_report_sold["Flag (>90% null)"] = null_report_sold["Null %"] > 90
null_report_sold = null_report_sold.sort_values("Null %", ascending=False)
null_report_sold

    # dropped columns with >90% missing values
drop_cols_sold = null_report_sold[null_report_sold["Flag (>90% null)"]].index
sold_resid = sold_resid.drop(columns=drop_cols_sold)

    # dropped additional 6 observations for missing closing price
sold_resid = sold_resid.dropna(subset=["ClosePrice"])

# Numeric distribution summary, Sold (min, max, mean, median, percentiles) for ClosePrice, LivingArea, and DaysOnMarket
cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket']

summary_sold = pd.DataFrame({
    'min': sold_resid[cols].min(),
    'max': sold_resid[cols].max(),
    'mean': sold_resid[cols].mean(),
    'median': sold_resid[cols].median(),
    '25%': sold_resid[cols].quantile(0.25),
    '75%': sold_resid[cols].quantile(0.75)
})
summary_sold


# Repeat for listing dataset
# Inspecting structure
list.columns

# Data snapshot
list.head()
list["PropertyType"].value_counts()

# Applying same residential classification and filter to listing data
list_resid = list[list["PropertyType"].isin(["Residential", "ResidentialLease", "ResidentialIncome"])]

# Validate completeness for listing data
null_report_list = pd.DataFrame({
    "Null Count": list_resid.isnull().sum(),
    "Null %": (list_resid.isnull().sum() / len(list_resid) * 100).round(2)
})
null_report_list["Flag (>90% null)"] = null_report_list["Null %"] > 90
null_report_list = null_report_list.sort_values("Null %", ascending=False)
null_report_list

# Apply same logic as sold of dropping columns w/ >90% missing values
# Did not drop observations with missing closing price as that is natural for listed property to not be sold
drop_cols_list = null_report_list[null_report_list["Flag (>90% null)"]].index
list_resid = list_resid.drop(columns=drop_cols_list)

# Numeric distribution summary, Listing (min, max, mean, median, percentiles) for ClosePrice, LivingArea, and DaysOnMarket
cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket']

summary_list = pd.DataFrame({
    'min': list_resid[cols].min(),
    'max': list_resid[cols].max(),
    'mean': list_resid[cols].mean(),
    'median': list_resid[cols].median(),
    '25%': list_resid[cols].quantile(0.25),
    '75%': list_resid[cols].quantile(0.75)
})
summary_list

# Save the filtered dataset as a new CSV (for different types of residential property types and drops)
list_resid.to_csv("w2_list_resid.csv", index=False)
sold_resid.to_csv("w2_sold_resid.csv", index=False)
