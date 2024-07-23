import pandas as pd

def clean_imdb_csv(input_file: str) -> pd.DataFrame:
    try:
        movies = pd.read_csv(input_file, encoding='iso-8859-1')
        print("File successfully read with ISO-8859-1 encoding.")
    except UnicodeDecodeError:
        print("Error: Unable to read file with ISO-8859-1 encoding. Please check the file encoding.")
        return None

    # Data Cleaning Steps
    movies = movies.dropna(subset=['Duration', 'Rating', 'Votes', 'Actor 1', 'Actor 2', 'Actor 3', 'Genre'])
    movies.drop_duplicates(keep='first', inplace=True)
    movies['Votes'] = movies['Votes'].str.replace(',', '')
    movies = movies.astype({'Votes': float})

    # Splitting Genre into two columns
    TempGenre = movies['Genre'].str.split(',', expand=True).iloc[:, 0:2]
    TempGenre.columns = ['Genre_1', 'Genre_2']
    TempGenre['Genre_2'].fillna(TempGenre['Genre_1'], inplace=True)
    movies = pd.concat([movies, TempGenre], axis=1)

    return movies

if __name__ == "__main__":
    input_file = r'D:\ETL_project\IMDb_Movies_India.csv'
    cleaned_df = clean_imdb_csv(input_file)
    if cleaned_df is not None:
        print(cleaned_df.head())
