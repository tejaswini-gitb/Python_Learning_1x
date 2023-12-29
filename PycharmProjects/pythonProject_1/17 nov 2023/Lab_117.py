import csv

data = [
    ['name','age','location','code'],
    ['avika',15,'pune',78],
    ['bavya',16,'pune',75],
    ['chetan',15,'bang',75]
]

with open('mydata.csv','w') as file:
    write = csv.writer(file)
    for row in data:
         write.writerow(row)