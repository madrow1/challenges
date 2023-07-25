
list = [5,23,6,8,3,2,643,7,8,3,16,45,2,35,67]

def sort_list(list,op):
    if op == "asc": 
        print("list is ascending")
        list.sort(reverse=False)
    elif op == "desc":
        print("list is descending")
        list.sort(reverse=True)
    elif op == "none" or op == "":
        print("list is none")
    else: 
        print("Please use on of the following: desc, asc or none")
    return list

sort_list(list,"")

print(list)
