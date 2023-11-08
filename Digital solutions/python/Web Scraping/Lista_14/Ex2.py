import requests
from bs4 import BeautifulSoup

site = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(site.text, 'html.parser')

citacoes = soup.find_all("span", class_= 'text') 
for cit in citacoes:
    print(cit.get_text())
