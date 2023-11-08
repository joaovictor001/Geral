import requests
from bs4 import BeautifulSoup


raspagem = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(raspagem.text, "html.parser")

selecao = soup.find_all("div", class_="tags")
for tag in selecao:
    print(tag.get_text())
