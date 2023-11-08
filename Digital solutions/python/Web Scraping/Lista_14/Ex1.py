import requests
from bs4 import BeautifulSoup

solicitação = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(solicitação.text , 'html.parser')

titulo= soup.title.string
print(titulo)