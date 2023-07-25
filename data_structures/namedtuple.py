import csv 
from collections import namedtuple

def order_fits(driver, num_packages):
    return driver.capacity >= num_packages

def main():
    
    Driver = namedtuple("driver", ["name","car","capacity"])

    iris = Driver("Iris","Pryus", 7)
    mickie = Driver("Mickie","Honda",9)

    print(order_fits(iris,7))
    return 

if __name__ == "__main__":
    main()

