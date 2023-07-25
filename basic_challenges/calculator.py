# Takes three params, two int and one string, and uses the eval operator to treat them as math
def calc(num1,operand,num2):
    concat = str(num1) + str(operand) + str(num2)
    return print(eval(concat))

calc("4","*","5")