# merging in tuples

hero1=("batman","bruce wayne")
hero2=("harry","diana")
team= hero1 + hero2
print(team)

# convert to list
 
my_tuple=(1,2,5,4,2)
print(list(my_tuple))

# nested tuple
hero11=("batman","bruce wayne")
hero21=("harry","diana")
team1= (hero11 , hero21)# (('batman', 'bruce wayne'), ('harry', 'diana'))
print(team1)
print(team1[1]) # ('harry', 'diana')
print(team1[0][1]) #bruce wayne
print(team1[1][0]) # harry
print(len(team1))# 2

# search
city=("paris","ohio","mosco","delhi")
print(city)
print("mumbai" in city) # false
print("paris" in city) #True

