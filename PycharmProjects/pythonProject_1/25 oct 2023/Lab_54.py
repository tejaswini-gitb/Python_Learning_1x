# map and filter in the list

# map functions
numbers= [1,2,3,4,5]
#sq_numbers=[1,4,9,16,25]
sq = lambda x: x * x
sq_numbers =[]

for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)

# map fuct

sq_numbers2= list (map(lambda x: x * x, numbers))
print(sq_numbers2)