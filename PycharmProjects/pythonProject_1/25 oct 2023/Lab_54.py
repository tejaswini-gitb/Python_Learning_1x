# map and filter in the list

# map functions  where we will go from one item and apply a function
numbers= [1,2,3,4,5]
sq_numbers=[1,4,9,16,25]
sq = lambda x: x * x
sq_numbers =[]


for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)

# map functions

sq_numbers2= list (map(lambda x: x * x, numbers))
print(sq_numbers)

def triple(a):
    return a* 3

sq_numbers=list(map(lambda x: x * 3, numbers))
sq_numbers2= list (map(triple , numbers))
print(sq_numbers2)
