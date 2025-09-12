import pandas as pd
def load_csv_data(file_path,data_type = 'heart_rate'):
    """
    Returns:
        pandas DataFrame with extracted data
    """
        

    try:
        df=pd.read_csv(file_path)
        print(f"Loaded{len(df)} rows from{file_path}")
        print("First 5 rows:")
        print(df.head())
        if 'timestamp' not in df.columns:
            raise ValueError("CSV must contain 'timestamp' column")
            df ['timestamp'] =pd.to_datetime(df['timestamp'],format="%y-%m-%d %H:%M:%S")

        print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return None
    except Exception as e:
        print(f"Error loading CSV: {str(e)}")

        return None
    


loaded_data=load_csv_data('sample_heart_rate.csv')
