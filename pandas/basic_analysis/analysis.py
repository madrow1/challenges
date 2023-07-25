import pandas as pd 

oo = pd.read_csv("../athlete_events.csv")

print(oo.Sex.value_counts()) # value counts counts how many instances of a specific value are in the frame, options such as ascending can be used to change the order the data is returned

print(oo.Sex.sort_values()) # sorts the contents of a column in ascending order 

ath = oo.sort_values(['Name','Medal'])

print(ath)