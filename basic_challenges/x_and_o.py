

def count_x_o(input):
    count_x = 0
    count_o = 0
    for letter in range(len(input)):
        if input[letter].lower() == "x":
            count_x += 1
        if input[letter].lower() == "o":
            count_o += 1

    if count_x != count_o:
        return False

    else:
        return True

print(count_x_o("xxoxoxoxoo"))