import csv 
from collections import namedtuple


def main():

    with open("Customer.csv", "r") as f:
        read = csv.reader(f)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)
            print(person)
            
    return 

if __name__ == "__main__":
    main()