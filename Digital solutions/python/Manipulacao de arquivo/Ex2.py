import csv
with open('meu_aquivo_csv.csv','w') as file:
    csv.writer(file,delimiter=',').writerow(['joao','30'])