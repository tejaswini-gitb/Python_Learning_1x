#palimdrome  (reverse strinng  23 oct)
# naman--- opp. naman

#user_input = input("enter the input= ")

def reverse_string(input_string):
    reverse_str= ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str

original_str="naman"
rev_str=reverse_string(original_str)
print(rev_str)


if original_str == rev_str:
    print("palindrome")
else:
    print("it is not")