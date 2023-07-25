# wisdom pet medicine website
# The request package is the standard python package for HTTP requests

#importeren 'requests' en 'bs4' pakkets
import requests 
from bs4 import BeautifulSoup

response = requests.get('https://wisdompetmed.com/')

# Print the reponse code of the server / druk de responscode van de server 
print(response.status_code)

# Print the headers recieved as part of the response / druk de headers van de server 
#print(response.headers)

# Print the content of the site / druk de inhoud van de site 
#print(response.content)

# Prints the HTML text of the site / druk de HTML-tekst van de site 
#print(response.text)

# Creates a new variable using the beautifulsoup package / maakt een nieuwe variabele met behulp van het pakket beautifulsoup
soup = BeautifulSoup(response.text)

# Prints the soup variable using the prettify package from beautifulsoup / drukt de soup variabele af met behult van het prettify-pakket van beautifulsoup 
#print(soup.prettify())

# Prints the output of HTML tags equal to 'title' / druk de uitvoer van HTML-tags af gelijk aan 'title'
print(soup.find('title'))

# Prints the output of HTML tags equal to 'article'  druk de uitvoer van HTML-tags af gelijk aan 'article' 
print(soup.find_all('article'))

# Prints the output of HTML tags equal to 'span'  druk de uitvoer van HTML-tags af gelijk aan 'span' 
print(soup.find('span', class_ = 'phone').text)

featured_testimonials = soup.find_all('div', class_ = 'quote')
#for t in featured_testimonials:
#    print(t.text)

links = soup.find_all('a')
for l in links:
    print(l.text, l.get('href'))