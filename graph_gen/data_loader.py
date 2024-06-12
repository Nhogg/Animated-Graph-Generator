# graph_gen/data_loader.py
import pandas as pd

def load_data(file_path):
    """
    Load data from an Excel or CSV file.
    
    Args:
    file_path (str): Path to the file.
    
    Returns:
    pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path, engine='openpyxl')  # Specify the engine here
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
