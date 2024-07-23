import pandas as pd
from sqlalchemy import create_engine
from config_db import DATABASE_CONFIG


# Create a connection to the PostgreSQL database
db_url = f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
engine = create_engine(db_url)

# Read the tables into pandas DataFrames
imdb_df = pd.read_sql("SELECT * FROM imdb_csv_data", engine)
excel_df = pd.read_sql("SELECT * FROM imdb_excel_data", engine)

# Display the first few rows of each DataFrame to understand their structure
print(imdb_df.head())
print(excel_df.head())

# Rename columns in excel_df for easier merging if necessary
excel_df.rename(columns={
    'movies name': 'name',
    'Rating out of 10': 'Rating',
    'Count of Rating': 'Votes'
}, inplace=True)

# Merge the DataFrames based on a common column 
merged_df = pd.merge(imdb_df, excel_df, left_on='Name', right_on='Movies Names', how='outer')

# Display the merged DataFrame
print(merged_df.head())

# Optional: Save the merged DataFrame back to the PostgreSQL database
merged_df.to_sql('merged_imdb_data', engine, if_exists='replace', index=False)
