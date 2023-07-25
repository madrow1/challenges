# Create a Python function that accepts a string. 
# The function should return a string, with each character in the original string doubled.
# If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.

def repeat_character(string,count):
    doubled = []
    for char in range(len(string)):
        doubled.append(string[char]*count)
        
    return print("".join(doubled))

repeat_character("test!",3)
