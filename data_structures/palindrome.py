from collections import deque



def main():

    ordered_foods = ["DES003", "STA002", "DES005", "ENT001"]



    def isPalindrome(ordered_foods):
        pallindromes = []
        for word in ordered_foods:
            if word == word[::-1]:
                pallindromes.append(word)
            else:
                continue
        return pallindromes
        
    return print(isPalindrome(ordered_foods))

if __name__ == ("__main__"):
    main()