# factorial

# n= 5
# 5*4*3*2*1
#
# 4! = 4*3*2*1


#---------------break

count =1
while count <= 10:
    print(count)
    if count >= 8:
        break
    count = count + 1

#---------------continue

for counter in range (1,10):
    if counter == 5:
        break
    print(counter)
print("for loop ")

#-------------
for i in range (1,15):
     if i == 9:
         pass   # 9 will skipped
     else:
         print(i)


         #--------------
for i in range(1,8):
    print(i)
    print("loop is finished")