import pandas as pd
import numpy as np 
import random

n=100

first_name=['akash','shubham','badal','mayank','anshul']
last_name=['gourav','sourabh','chauhan','mohit','rohit']

def generate_indian_name():
  first=random.choice(first_name)
  last=random.choice(last_name)
  return f"{first} {last}"

data={
    'player_ID':range(1,n+1),
    'Name':[generate_indian_name() for _ in range(n)],
    'Role':np.random.choice(['Batsman','Bowler','all-rounder','wicketkeepaer'],n),
    'Batting_Average': np.random.uniform(20, 50, n),
    'Strike_Rate': np.random.uniform(80, 150, n),
    'Bowling_Average':np.random.uniform(25, 45, n),
    'Economy_Rate':np.random.uniform(3, 6, n),
    'Catches': np.random.uniform(0, 20, n),
    'Recent_form':np.random.uniform(10, 100, n),
    'Match_Condition':np.random.choice(["Sunny", "Cloudy", "Rainy", "Humid"]),
    'Match_impat_Score':np.random.uniform(0, 10, n)
    }

df=pd.DataFrame(data)

df.head(1000)
df.tail()


