import pandas as pd 

oo = pd.read_csv("C:/Users/rowan/python_pandas/athlete_events.csv")

print(oo.shape) # returns the shape of the data frame as a tuple 

print(oo.head()) # prints the first lines of a CSV, can use (x) to specify how many rows to show, as in Linux 

print(oo.tail()) # prints the last lines of a CSV, can use (x) to specify how many rows to show, as in Linux 

print(oo.info()) # returns info on the different data types in the frame 