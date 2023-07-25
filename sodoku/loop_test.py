#%%

import random

size = 9

row = []

for i in range(1,size+1):
    rand = random.randint(1,size)
    if ('║ ' + str(rand) + ' ║') not in row:
        row.append('║ ' + str(rand) + ' ║')
    else:
        row.append('║ ' + " " + ' ║')    


print(row)
# %%