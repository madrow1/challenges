import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns

# different kinds of plot() exist, they can be specified with a kind= key word
# plot(kind='line'), plot(kind='bar'), plot(kind='barh'), plot(kind='pie'), by default it is line 

oo = pd.read_csv('../athlete_events.csv')

fo = oo[(oo.Year == 1992) & (oo.Sex == 'F')] # grabbing a random years worth of data to plot 

fo.Event.value_counts()

#Then to plot that data to a graph use dot notation

fo.Event.value_counts().plot(kind='bar', color = 'maroon', figsize=(10,3));

# Colours can be specified with colour = inside the .plot()

# figsize = is a tuple that can be used to change the size of the graph scale

# Color maps are used to map data to logical colours

# seaborn can be used to make plots more legible and adds a greater range of plots 

print(sns.countplot(x='Medal', data=oo))

print(sns.countplot(x='Medal', data=oo, hue='Sex'))
