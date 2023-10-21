x=100
y=1006
z=522

maxx=None

if x > y and x > z:
    maxx= x
elif y > x and  y > z:
    maxx = y
else:
    maxx = z

print(maxx)

