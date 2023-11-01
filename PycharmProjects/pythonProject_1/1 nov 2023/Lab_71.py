numlist=[22,-9,91,0,14,-4,85,55,-99,76,-8,49]

def num_grt_50(num):
    return num >70

op=list(filter(num_grt_50,numlist))
print(op)


# with lambda

numlist={22,-9,91,0,14,-4,45,55,-99,66,-8,51}

def num_grt_50(num):
    return num > 40

op=list(filter(lambda num: num>50, numlist))
print(op)


#possible with list and tuple, dict

