def hide_number(num):
    count = 0
    hidden = []
    if len(str(num)) > 16: 
        print("This is not a credit card number")
    else:
        for number in str(num): 
            if count < 4:
                hidden.append(number)
                count +=1
            else: 
                hidden.append("*")
        return print(" ".join(hidden))

hide_number(2479563456346634)

