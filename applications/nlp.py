

with open('/Users/rpitt/challenges/applications/expectations.txt', 'r', encoding='utf-8') as file:
    great_expect = file.read()

#imporeten het NLTK pakkets
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

# imporeten het gensim pakkets
from gensim.corpora import dictionary
from gensim.models import ldamodel
from gensim.models.coherencemodel import CoherenceModel
from wordcloud import WordCloud

# imporeteer de andere pakket 
import pandas as pd 
from PIL import Image 
import numpy as np 
import random 
import matplotlib.pyplot as plt
import re

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('vader_lexicon')
#nltk.download('wordnet')

word_cloud_text = great_expect.lower()

word_cloud_text = re.sub("(^a-zA-Z0-9)", " ", word_cloud_text)

tokens = word_tokenize(word_cloud_text)

tokens = (word for word in tokens if word not in stopwords.words("english"))

tokens = (word for word in tokens if len(word) >=3)

#Data cleaning to split data into sentences
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"

text = " " + great_expect + "  "
text = text.replace("\n"," ")
text = re.sub(prefixes,"\\1<prd>",text)
text = re.sub(websites,"<prd>\\1",text)
text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
if "..." in text: text = text.replace("...","<prd><prd><prd>")
if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
if "”" in text: text = text.replace(".”","”.")
if "\"" in text: text = text.replace(".\"","\".")
if "!" in text: text = text.replace("!\"","\"!")
if "?" in text: text = text.replace("?\"","\"?")
text = text.replace(".",".<stop>")
text = text.replace("?","?<stop>")
text = text.replace("!","!<stop>")
text = text.replace("<prd>",".")
sentences = text.split("<stop>")
sentences = [s.strip() for s in sentences]
sentences = pd.DataFrame(sentences)
sentences.columns = ['sentence']

print(len(sentences))
#print(sentences.head())

print(sentences.drop(sentences.index[:59], inplace=True ))

sentences = sentences.reset_index(drop=True)

print(sentences.head())

stopwords_wc = set(stopwords.words('english'))

wordcloud = WordCloud(max_words=100, stopwords=stopwords_wc,random_state=1).generate(word_cloud_text)
plt.figure(figsize=(12,16))
plt.axis('off')
##plt.imshow(wordcloud)
#plt.show()

#fdist = nltk.FreqDist(tokens)

#plt.figure(figsize=(12,6))
#fdist.plot(50)
#plt.show()

analyzer = SentimentIntensityAnalyzer()

sentences['compound'] = [analyzer.polarity_scores(x)['compound'] for x in sentences['sentence']]
sentences['neg'] = [analyzer.polarity_scores(x)['neg'] for x in sentences['sentence']]
sentences['neu'] = [analyzer.polarity_scores(x)['neu'] for x in sentences['sentence']]
sentences['pos'] = [analyzer.polarity_scores(x)['pos'] for x in sentences['sentence']]

print(sentences.head())


