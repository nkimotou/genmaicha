import pandas as pd
import open_source_datasets

"""
This is a very simple script that handles open source data about caffeine content in popular drinks.
In particular, we investigate the differences in caffeine content in tea drinks.
This is a smaller dataset that is filtered down using 
"""

# Set file path for import
file_path = open_source_datasets.caffeine_content

# Read the csv file into a pandas DataFrame
cf_df = pd.read_csv(file_path)

# Filter down to tea columns
cf_df = cf_df[cf_df['type'] == 'Tea']

# Filter tea type column for tea drinks with greater than 50mg caffeine
cf_df = cf_df[cf_df['Caffeine (mg)'] > 50]

# Filter tea type by drinks with less than 50 calories
cf_df = cf_df[cf_df['Calories'] < 50]

# Trim columns
cf_df = cf_df[['drink', 'Calories', 'Caffeine (mg)']]

# fix drink column that was lowercase
cf_df.rename(columns={'drink': 'Drink'}, inplace=True)

# Print data without row numbers from original CSV data
print(cf_df.to_string(index=False))


