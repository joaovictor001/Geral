import requests
from bs4 import BeautifulSoup

raspagem = requests.get("https://quotes.toscrape.com")
soup  = BeautifulSoup(raspagem.text, "html.parser")
print("Albert Einstein \nJ.K. Rowling\nAlbert Einstein \nJane Austen\nMarilyn Monroe\nAlbert Einstein\nAndré Gide\nThomas A. Edison\nEleanor Roosevelt\nSteve Martin")

autor_escolhido = input("Qual o autor escolhido: ")

citacoes = soup.find_all('span', class_="text")
for c in citacoes:
    author = c.find_next("small", class_="author")
    if author and author.get_text() == autor_escolhido:
        print(c.get_text())

