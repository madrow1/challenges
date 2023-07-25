#stacking and unstacking, stacking lets you sort athletes into custom data frames, multiple elements can be used, the stack() function will combine similar elements 

import pandas as pd 

oo = pd.read_csv('../athlete_events.csv')

print(oo[(oo.Year == 2000) & (oo.Sport == "Basketball")])