my_di={}
print(my_di)
print(type(my_di))

my_di1={"batman":"oui","superman":4885,"spiderman":949,"spiderman":948}    # latest value is printed
print(my_di1)
keys=my_di1.keys()
print(keys)
values=my_di1.values()
print(values)
print(len(my_di1))
# no indexing
# print(my_di1[1])
print(my_di1["batman"])

turk=dict(lang="turkish",ppl=234,wm=445,chl=342)
print(turk)
print('chl')
print("ppl")
print(turk.get("chl"))
print(turk["wm"])