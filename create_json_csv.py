import numpy as np
from datetime import datetime, timedelta
import json

def create_sample_json_data():
    fitness_data={
        "user_id":"user_123",
        "device":"Fitness Tracker pro",
        "export_date": datetime.now().strftime('%Y-%m-%d'),
        "heart_rate_data":[],
        "step_data":[],
        "sleep_data":[]
    }
    

    start_time=datetime.now().replace(hour=8,minute=0,second=0,microsecond=0)
    for i in range(60):
        timestamp = start_time + timedelta(minutes=i)
        hr = 70 + np.random.normal(0, 8)
        fitness_data["heart_rate_data"].append({
            "timestamp": timestamp.isoformat(),
            "bpm": max(50,min(150,int(hr))),
            "confidence":np.random.uniform(0.8,1.0)
        })
    for i in range(60):
        timestamp=start_time+timedelta(minutes=i)
        steps=np.random.poisson(12)
        fitness_data["step_data"].append({
            "timestamp":timestamp.isoformat(),
            "steps":steps,
            "cadence":steps*60 if steps > 0 else 0
        })
    with open('sample_fitness_data.json','w') as f:
        json.dump(fitness_data,f,indent=2)
    print('created file')
    return fitness_data
json_data=create_sample_json_data()