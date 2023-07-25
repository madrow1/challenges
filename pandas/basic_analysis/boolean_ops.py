# in pandas the standard AND, OR and NOT are &, | and !
import pandas as pd 

oo = pd.read_csv('../athlete_events.csv')

#print(oo[oo.Medal == 'Gold']) # To evaluate a data frame against itself the data frame should be inside [] so in this case oo[oo.EVAL == 'x']

#print(oo[(oo.Medal == 'Gold') & (oo.Sex == 'F')]) # multiple boolean operators can be used in a single expression to evaluate against eachother 

# standard string methods can be used with the pd object 

#print(oo[oo.Name.str.contains('Florence')]) 

#Challenges 

# In which events did Florence Allan win a medal 
print(oo[oo.Name.str.contains('Florence Allan')])

# Which country has won the most golds in Athletics
gold = oo[(oo.Medal == 'Gold') & (oo.Sport == 'Athletics') & (oo.Sex == 'M')]

print(gold.value_counts('Team'))

track = oo[(oo.Event.str.contains('100')) & (oo.Sport == 'Athletics') & (oo.Sport != 'Relay')]

print(track)