# Data Collection

import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' could not be parsed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
        return None