from collections import namedtuple
import default_dict
from pprint import pprint

def get_dict(list_to_sort):
    res = default_dict(lambda: set())
    for item in list_to_sort:
        cat = item.identifier[0:3]
        
        match cat:
            case "PIZZA":
                res["Foood"].add(item)
            case "MOREPIZZA":
                res["TASTY"].add(item)

def main():
    Food = namedtuple("Food", ["ID", "name"])

    list = [
        Food("PIZZA", "Pizza")
        Food("MOREPIZZA", "Its pizza time")
    ]

    pprint(dict(get_dict(list)))
    return

if __name__ == "__main__":
    main()