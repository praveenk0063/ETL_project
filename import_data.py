import pandas as pd
from sqlalchemy import create_engine
from config_db import DATABASE_CONFIG
from imdb_csv import clean_imdb_csv
from imdb_excel import clean_excel

def get_db_connection():
    # Create the database connection
    db_url = f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    engine = create_engine(db_url)
    return engine

def import_df_to_db(df: pd.DataFrame, table_name: str):
    # Get the database connection
    engine = get_db_connection()

    # Import the data to the specified table
    df.to_sql(table_name, engine, if_exists='replace', index=False)

if __name__ == "__main__":
    # Clean the CSV data and import to database
    csv_input_file = r'D:\ETL_project\IMDb_Movies_India.csv'
    cleaned_csv_df = clean_imdb_csv(csv_input_file)
    import_df_to_db(cleaned_csv_df, 'imdb_csv_data')

    # Clean the Excel data and import to database
    excel_input_file = r'D:\ETL_project\IMDB_Top250_Movies.xlsx'
    cleaned_excel_df = clean_excel(excel_input_file)
    import_df_to_db(cleaned_excel_df, 'imdb_excel_data')