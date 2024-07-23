import subprocess

def run_scripts():
    # Run the imdb_csv_file.py script to clean and import CSV data
    subprocess.run(['python', 'import_data.py'])
    subprocess.run(['python', 'merge_data.py'])

if __name__ == "__main__":
    run_scripts()
