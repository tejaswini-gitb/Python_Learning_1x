import csv

my_data= []
id_update=2
new_age =26

with open ('file.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        my_data.append(row)


#for row in my_data:
 #   print(row)
  #  if row[0] == id_update:
   ##     row[1] = new_age

my_data[2][2] =28
print(my_data)

with open('file.csv','w', newline ='') as csvfile:
    writer= csv.writer(csvfile)
    writer.writerows(my_data)