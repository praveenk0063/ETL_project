import pandas as pd
import re

def convert_currency(currency_str):
    currency_str = str(currency_str)
    numerical_part = re.sub(r'[^0-9]', '', currency_str)
    if numerical_part:
        return float(numerical_part)
    else:
        return None

def clean_excel(input_file: str) -> pd.DataFrame:
    try:
        imdb = pd.read_excel(input_file)
        print("File successfully read.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

    # Drop rows with missing values
    imdb = imdb.dropna(how='any')
    
    # Cleaning and converting currency columns
    for column in ['Budget', 'Worldwide Gross', 'Domestic Weekend', 'Domestic Gross2']:
        imdb[column] = imdb[column].str.replace(',', '').str.replace('$', '').apply(convert_currency)
    
    # Convert values to millions
    imdb['Budget'] = imdb['Budget'] / 1000000
    imdb['Worldwide Gross'] = imdb['Worldwide Gross'] / 1000000
    
    # Calculate profit
    imdb['Profit'] = imdb['Worldwide Gross'] - imdb['Budget']
    
    # Sort values by profit
    imdb = imdb.sort_values(by='Profit', ascending=False)

    return imdb

if __name__ == "__main__":
    input_file = r'D:\ETL_project\IMDB_Top250_Movies.xlsx'
    cleaned_df = clean_excel(input_file)
    if cleaned_df is not None:
        print(cleaned_df.head())
