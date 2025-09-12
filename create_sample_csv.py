import pandas as pandas
import numpy as np
from datetime import datetime, timedelta


print("Lets start building data")

def create_sample_csv(file_path,num_rows=100):
    """create sample """
    start_time=datetime.now().replace(hour=10,minute=0,second=0,microsecond=0)
    timestamps=[]
    heart_rates=[]
    for i in range(120):
        timestamp = start_time + timedelta(minutes=i)
        base_hr = 75 + np.sin(i / 30) * 30
        noise = np.random.normal(0, 5)
        hr = max(50, min(120, base_hr + noise))
        timestamps.append(timestamp.strftime('%y-%m-%d %H:%M:%S'))
        heart_rates.append(hr)
    df = pandas.DataFrame({'timestamp': timestamps, 'heart_rate_bpm': heart_rates})
    df.to_csv('sample_heart_rate.csv', index=False)
    print("Created sample_heart_rate.csv")
    return df
hr_data=create_sample_csv("C://Users//RELIANCE//OneDrive//Desktop//9. analysis and detection of autism spectrum//AutismScreening//aa.csv")
print(hr_data.head)

