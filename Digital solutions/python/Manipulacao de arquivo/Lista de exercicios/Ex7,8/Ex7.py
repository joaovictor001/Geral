import xml.etree.cElementTree as ET
root = ET.Element("Quimicos")

quimico1 = ET.SubElement(root, "Hidrogenio")
quimico1_symbol = ET.SubElement(quimico1, "Simbolo")
quimico1_symbol.text = "'H'"

quimico1_atomic_number = ET.SubElement(quimico1, "NumeroAtomico")
quimico1_atomic_number.text = "1"

quimico2 = ET.SubElement(root, "Oxigenio")
quimico2_symbol = ET.SubElement(quimico2, "Simbolo")
quimico2_symbol.text = "'O'"

escreva = ET.ElementTree(root)


with open("elementos.xml","wb") as myfile:
    escreva.write(myfile, encoding="utf-8", xml_declaration=True)
print("Tudo isso pra criar um arquivo ")
print("Mas fiz :D")