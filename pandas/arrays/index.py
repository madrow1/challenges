import pandas as pd 

oo = pd.read_csv('../athlete_events.csv')

#print(oo.index[106]) # Panda indexes are immutable, i.e. the contents of the index cannot be changed 

#print(oo.head())

oo.set_index('ID', inplace=True) # set_index can be used to change the element that is used as an index, inplace= must be used to make that change persistent 

ath = oo

print(ath.sort_index(inplace=True)) # by default the index will be sorted into alphabetical or numberical, this can be reversed with ascending=False

print(ath.head())

oo.reset_index(inplace=True) # resets the index to the original element

print(oo.loc[34]) #returns the index value in the square brackets

print(oo.City == 'Lillehammer') # == can be used to search where the index is not the value you want to search for 

print(oo.iloc[[77,35,155]]) # iloc can be used to search for lists, and can use python list slicing [:]

