
l1 = [2,4,6,2,7,1]
l2 = [3,6,1,7,8,2]


def offset(list,fill,offset=0):
    result = []
    first_list = []
    l1 = list
    l2 = fill
    if offset >= 1:
        for i in range(offset):
            l1.append("*")
            l2.insert(i,"*")
        result = [[f, fi] for f, fi in zip(l1,l2)]


    else:
        result = [[i, j] for i, j in zip(list,fill)]
    
    return result 

print(offset(l1,l2))