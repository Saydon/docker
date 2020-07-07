# /usr/bin/python3
import requests
import json
from time import sleep

def getBitcoinPrice():
    URL = "http://www.bitstamp.net/api/ticker/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

#Get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 

#Description: Get the current price of Bitcoin every minute and average price of the last 10 minutes
prices = []
i = 0 
while True:
    bitPrice = getBitcoinPrice()
    print("Bitcoin last price: $" + str(bitPrice) + "/BTC")
    prices.append(bitPrice)
    sleep(60)
    i = i+1
    if i == 10:
        print("Bitcoin average price of the last 10 minutes: $" + str(Average(prices)) + "/BTC")
        prices = []
        i = 0