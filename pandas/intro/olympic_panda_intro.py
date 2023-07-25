import pandas 
import pandas as pd 

oo = pd.read_csv("C:/Users/rowan/python_pandas/athlete_events.csv") # reads the CSV file into the object oo 
oo.head()

print(oo.Name) # elements of the panda object can be called with dot notation 
print(oo['Name']) # or with ['element name ']

print([['ID', 'Name', 'Age']]) # multiple elements can be called at once with [['','']]

print(type(oo))
print(type(oo['Name']))