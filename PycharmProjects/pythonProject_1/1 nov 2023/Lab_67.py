# filter
# even num
numbers=[1,2,-3,4,5,-13,7,8,-9,10,-11,12]
def is_even(numbers):
    return numbers % 2 == 0
op= is_even(2)  # divided by num 2
print(op)
# output --true or false

even_num=filter(is_even,numbers)
print(even_num)
even_num_list=list(even_num)
print(even_num_list)

# positive

def is_pos(numbers):
    return numbers > 0

pos_num=filter(is_pos,numbers)
print(pos_num)
is_posnum_list=list(pos_num)
print(is_posnum_list)