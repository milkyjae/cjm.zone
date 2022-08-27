import requests
from bs4 import BeautifulSoup
import webbrowser
import time


# def getData(symbol): 
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
#     url = f'https://www.coindesk.com/price/{symbol}'
#     r = requests.get(url, headers)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     stock = {
#     'symbol': symbol,
#     'price': soup.find('div', {'class':'Box-sc-1hpkeeg-0 jwYVXk'}).find_all('span')[1].text, 
#     'change': soup.find('div', {'class':'Box-sc-1hpkeeg-0 keDxjI'}).find_all('h6')[0].text, 
#     }
#     return stock; 


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
url = 'https://www.coindesk.com/price/bitcoin'
r = requests.get(url, headers)
soup = BeautifulSoup(r.text, 'html.parser')
     
price = soup.find('div', {'class':'Box-sc-1hpkeeg-0 jwYVXk'}).find_all('span')[1].text 
pchange = soup.find('div', {'class':'Box-sc-1hpkeeg-0 keDxjI'}).find_all('h6')[0].text 

btc = "$" + price


print(btc)

file = open('btc-price.txt', 'w')
file.write(btc)