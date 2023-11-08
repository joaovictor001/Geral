import json
with open("info.json", "r") as myfile:
    leitura = json.load(myfile)
animais = leitura['Animal']
nomee = leitura['Nome']
print(animais,nomee)
