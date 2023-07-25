# Imports time and random modules so that they can be used inside the program 
import random, time

def waiting_game():
    # Generic prettying stuff that doesn't impact the program at all 
    print("\n\n")
    print("Welcome to the waiting game")
    print("\n\n")
    print("Please wait the below number of seconds:")
    # All user inputs are considered as part of the program from here 
    input()

    # randomly assigns the variable waiting time a value between 1 and 4 when the user makes an input 
    waiting_time = random.randint(1,4)
    # Sets the variable start to the value of time when the user makes a second input
    start = time.time()
    input("Please wait for " + str(waiting_time) + " seconds")
    # Sets the value of end to the value of the current time on user input
    end = time.time()

    elapsed = end - start 

    difference = abs(round(waiting_time - elapsed,2))

    print("You were " + str(difference) + " seconds out")

    if difference < 0.5: 
        print("\n\n")
        print("Good job, very close")
    else: 
        print("\n\n")
        print("Could have done better :) ")


# Infinite loop so that the game never ends 
while True: 
    waiting_game()