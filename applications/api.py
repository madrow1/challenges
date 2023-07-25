
with open('./key.txt') as file:
    API_key = file.read()
API_key = API_key.strip()

# importeren pakkets van "alphavantage", 'requests', 'b24', 'pandas' en 'io'
from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import io 


ts1 = TimeSeries(key = API_key)

# druk de 'ts1' variabele met de functie 'get_monthly' 
#print(ts1.get_monthly("AAPL"))

# druk de 'ts1' variabele met de functie 'get_daily' 
#print(ts1.get_daily("AAPL"))

# druk de 'ts1' variabele met de functie 'get_intraday'
# print(ts1.get_intraday("AAPL"))

# The interval can be changed to either 5,15,30 or 60 minute intervals. / het interval kan worden gewijzigd in 5, 15, 30 of 60 minuten
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=15min&apikey=' + str(API_key) + '&datatype=csv'

r = requests.get(url).content

#data = r.json()

#data = BeautifulSoup(r.content)

#data = BeautifulSoup(r.content)

data = pd.read_csv(io.StringIO(r.decode('utf-8')))

# druk de 'data' variabele
print(data)
