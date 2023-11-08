import requests
from bs4 import BeautifulSoup

raspagem = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(raspagem.text, "html.parser")

autores = soup.find_all("small", class_='author')
for autor in autores:
    print(autor.get_text())