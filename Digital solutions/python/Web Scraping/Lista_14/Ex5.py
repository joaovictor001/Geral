import requests
from bs4 import BeautifulSoup

autor_escolhido = 'Jane Austen'
response = requests.get('http://quotes.toscrape.com')

soup = BeautifulSoup(response.text, 'html.parser')

   
quotes = soup.find_all('span', class_='text')
 
for quote in quotes:
    author_tag = quote.find_next('small', class_='author')
    if author_tag and author_tag.get_text() == autor_escolhido:
        print(quote.get_text())


