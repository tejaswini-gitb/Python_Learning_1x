with open ('read.txt', 'r') as file:
    content = file.read()
    print(content)


with open('read.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line,end='')