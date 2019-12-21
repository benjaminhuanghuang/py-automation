import requests
url = "http://quotes.toscrape.com"
response = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote in quotes:
  print(quote.text)

