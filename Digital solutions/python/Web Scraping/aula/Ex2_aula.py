import requests

from bs4 import BeautifulSoup 

response = requests.get("https://www.w3schools.com/")
soup = BeautifulSoup(response.text, "html.parser")
titulo  = soup.title.string
print("o titulo ",titulo)