def pallindrome_check(word):
    word = word.lower()
    if word[::-1] == word:
        return True
    else:
        return False


word = input("Please enter a word: ")

print(pallindrome_check(word))