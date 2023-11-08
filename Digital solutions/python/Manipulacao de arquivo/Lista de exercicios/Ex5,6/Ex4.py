import json

infos= {
    'Animal': ["Gato", "Cachorro"],
    'Nome': ["Felix", "Rexx"]


}
with open("info.json", "w") as myfile:
    json.dump(infos, myfile, indent=4)