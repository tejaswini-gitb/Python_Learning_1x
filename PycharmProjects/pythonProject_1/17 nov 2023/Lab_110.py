# text file

try:
    with open("textdata.txt", 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError as error:
    print(error)