import pandas as pd
import json

def load_json_data(file_path,extract_type='heart_rate'):
    try:
        with open(file_path,'r') as f:
            data=json.load(f)
        print(f"JSON file loaded. Available data types: {data.keys()}"
              )
        if extract_type == 'heart_rate':
            records=data.get('heart_rate_data',[])
            df=pd.DataFrame(records)
            if not df.empty:
                df['timestamp']=pd.to_datetime(df['timestamp'])
        elif  extract_type=='steps':
            records=data.get('step_data',[])
            df=pd.DataFrame(records)
            if not df.empty:
                df['timestamp']=pd.to_datetime(df['timestamp'])
        else:

            raise ValueError(f"Unsupported extract_type:{extract_type}")
        print(f"Extracted {len(df)} {extract_type} records")
        return df
    except FileNotFoundError:
        print(f"Error:File{file_path} not found")
        return None
