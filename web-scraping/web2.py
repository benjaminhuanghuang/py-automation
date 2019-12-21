import requests
url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')


items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for i in items:
  itemName = i.find('h4', class_='card-title').text
  itemPrice = i.find('h5').text

pages = soup.find('ul', class_='pagination')
urls=[]
links = pages.find_all('a', class_='page-link')
for link in links:
  pageNum = int(link.text) if link.text.isdigit() else None
  