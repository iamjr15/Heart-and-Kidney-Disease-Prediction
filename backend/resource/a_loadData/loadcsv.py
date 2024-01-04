import pandas as pd

def load_csv(topic):
    df = pd.read_csv(f"BackEnd/resource/topics/{topic}/input/train/{topic}.csv")
    
    return df