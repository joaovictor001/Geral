import requests
from bs4 import BeautifulSoup

raspagem = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(raspagem.text, 'html.parser')

citacoes = soup.find_all('span',class_='text')
autores = soup.find_all('small',class_='author')
tag = soup.find_all('div', class_='tags')

for i in range(len(citacoes)):
    quote_text = citacoes[i].get_text()
    author_name = autores[i].get_text()
    tagss = tag[i].get_text()
    print(f'Author: {author_name}\nQuote: {quote_text}\n')
    print(tagss)


