# palimdrome
original_str=input("enter name:")
#original_str= 'madam'

rev_str = original_str[::-1]
print(rev_str)

if original_str == rev_str:
    print("palindrome")
else:
    print("not a palindrome")
