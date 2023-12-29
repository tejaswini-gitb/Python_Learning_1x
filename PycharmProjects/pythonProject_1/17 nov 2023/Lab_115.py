# csv - format

import csv

with open ('Book1.csv',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print('_'. join(row))
        print(row[1],row[3],sep='|')
        print(row[1])