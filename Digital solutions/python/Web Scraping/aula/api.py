import requests
url="https://viacep.com.br/ws/01001000/json/"

response = requests.get(url)

if response.status_code == 200:
    data=response.json()
    print(data)
else:
    print("Erro ao buscar imformação de CEP", response.status_code)