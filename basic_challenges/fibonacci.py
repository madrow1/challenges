def fib(terms):
    n1, n2 = 0,1
    count = 0
    seq = []
    while count < terms: 
        print(count)
        nth = n1 + n2
        n1 = n2 
        n2 = nth
        seq.append(nth)
        count += 1
    return seq


print(fib(20))