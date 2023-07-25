def factorial(n):
    flag = True
    try:
        int(n)
    except ValueError:
        print("The value entered is not an integer")
        flag = False 


    if flag == False:
        quit()  
    else: 
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


print(factorial(1.2))