
string = "Ouija"

# Takes a single param as input, compares the characters in that string to a list of vowels and if the vowels match iterates the count variable which is then returned #

def count_vowel(input):
    count = 0
    for i in range(len(input)):
        if input[i].lower() in ["a","e","i","o","u"]:
            count += 1
        else:
            continue
    return print(count)

count_vowel(string)