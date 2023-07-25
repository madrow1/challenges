import random 
# Allows for the use of the Counter function 
from collections import Counter
import time

def dice(rolls,sides,dice_count):
    recorded_rolls = []
    started = time.time()
    # Multiplies the number of sides by the number of dice could be modified to accept different types of dice
    total_sides = sides * dice_count
    for roll in range(rolls):
        # Adds every single roll of the dice to a list, to simulate every possible outcome
        recorded_rolls.append(random.randint(1,total_sides))
    #print(recorded_rolls) # debug 

    # Counts the number of unique items in the list "recorded_rolsl"
    dict_items = Counter(recorded_rolls).items()
 
    # Orders the newly created dict_items dictionary to make it more readable for humans
    dict_items_sorted = dict(sorted(dict_items))

    # print(dict_items_sorted) # debug

    # Loops over every entry in dict_items_sorted and calculates the percentage liklihood of that result
    for unique, index in dict_items_sorted.items():
       print("The percentage chance of " + str(unique) + " is: " + str(index/rolls * 100) + "%")

    completed = time.time()
    total_time = completed - started 
    print("It took: " + str(total_time) + " seconds to complete this calculation")

dice(10000000,20, 1)