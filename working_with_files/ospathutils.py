import os
from os import path
import datetime
from datetime import date, time, timedelta
import time 

def main():
    # Check the OS of the system
    print(os.name)
    # Check if item exists and type
    print("Item exists: ", str(path.exists('file.txt')))
    print("Item is a file: ", str(path.isfile('file.txt')))
    print("Item is dir: ", str(path.isdir('file.txt')))
    # Find the path of an item
    print("Items path is: ", str(path.split(path.realpath('file.txt'))))
    # Get modification of the file
    t = time.ctime(path.getmtime("file.txt"))
    print("File was last modified at: ", t)
    print("File was last modified at: ", datetime.datetime.fromtimestamp(path.getmtime("file.txt")))
    # Returns the current time
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file.txt"))
    print("It has been ", td, " since the file was modified")
    return 0



if __name__ == "__main__":
    main()