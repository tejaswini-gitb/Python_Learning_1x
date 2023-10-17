#string
#bunch of char

name="TeJU"
print(name)

#string functions
#python functions is immutable in nature- can't be changed
#name[0]='k'
#str object doesn't suppoet item assignment

#--------------------------------------
#capitalized
#first letter is capital remaings are small letter

result=name.capitalize()
print(result)

#UPPER CASE-ALL CHAR IN UPPER
result1=name.upper()
print(result1)
print(id(result1))

#lower case- all in lower case
result2=name.lower()
print(result2)
print(id(result2))

#Title-
#each first letter of word is capital letter
name1='hello inDIA'
print(name1.title())

#len
print(len(name))

#replace
text='hello world'
result_rep=text.replace("world","python")
print(result_rep)

# find
# returns the lowest index of a substring in the string
#returns

text='hello world'
index=text.find('world')
print(index)

#h e l l o   w o r l d
#0 1 2 3 4 5 6 7 8 9 10

#count- count letters
count=text.count("l")
print(count)