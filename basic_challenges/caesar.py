import string


#Takes in a single param, the string to be ciphered, converts it all to lower case, creates a list to hold the full alphabet
#Transposes the letters of the cipher variable by +1 by comparing to the alphabet list and then returns the joined string.
def caesar(cipher):
    cipher = cipher.lower()
    encrypted = []
    alphabet = list(string.ascii_lowercase)
    for i in cipher:
        for l in range(len(alphabet)):
            if i == alphabet[l]:
                encrypted.append(alphabet[l+1])
    return "".join(encrypted)

print(caesar("This is a test"))