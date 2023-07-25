from collections import Counter
import numpy as np
import pandas as pd 

def unique_words(path):
    ls = []
    with open(path, "r") as f:
        count = 0 
        lines = f.readlines()
        
        for word in lines:
            total_length = len(word.split())

        for i in word.split(): 
            ls.append(i)


    unique_words = pd.value_counts(np.array(ls))      
    
    print("There are: " + str(total_length) + " words in this list")
    
    print("Top 20 words: ")
    print(unique_words[unique_words.values <= 1])

unique_words('test.txt')