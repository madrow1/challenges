


def decimal_to_binary(convert):
    
    binary = [0,0,0,0,0,0,0,0,0,0]

    for count in range(10,0,-1):

        square = 2**(count-1)

        if convert - square >= 0:
            binary[count-1] = 1
            convert -= square
        else:
            continue

    return print(binary[::-1])

decimal_to_binary(345)

