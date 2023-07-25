import pandas as pd 

oo = pd.read_csv("../athlete_events.csv")

type(oo.groupby("Name"))

for group_key,group_value in oo.groupby("Name"):
    print(group_key)
    print(group_value)