# map and filter in the list

# map functions
numbers= [1,2,3,4,5]
sq_numbers=[1,4,9,16,25]
sq_numbers = lambda x: x * 2
sq_numbers =[]


for i1 in numbers:
    sq_numbers.append(sq_numbers(i1))

print(sq_numbers)

# map functions

sq_numbers2= list (map(lambda x: x * x, numbers))
print(sq_numbers2)