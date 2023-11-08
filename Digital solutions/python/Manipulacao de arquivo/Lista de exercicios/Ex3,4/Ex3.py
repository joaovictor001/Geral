import csv

data = [["João", 30], ["Maria", 25]]

with open("alunos.csv", "w", encoding="utf-8", newline="") as myfile:
    writer = csv.writer(myfile)
    writer.writerows(data)
