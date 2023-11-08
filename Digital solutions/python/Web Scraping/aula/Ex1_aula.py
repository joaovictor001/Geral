import requests
responde  = requests.get("https://www.youtube.com/")
conteudo = responde.text
print("conteudo da pagina ")
print(conteudo)