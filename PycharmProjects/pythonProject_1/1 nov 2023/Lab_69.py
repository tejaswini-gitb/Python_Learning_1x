# 1
products=[
    {"name" : "laptop", "price" : 10000},
    {"name" : "pen", "price" : 200},
    {"name" : "bag", "price" : 500},
    {"name" : "wire", "price" : 800},
    {"name" : "sheet", "price" : 100},
    {"name" : "headphone", "price" : 100},
    {"name" : "phone", "price" : 1000},
    {"name" : "phone", "price" : 150},
]

print(products)
print(type(products))   # list
print(type(products[1:0]))  # dict
print((products[1:1]))  # []

def is_affordable(items):
    return items["price"] > 200

is_affordable=list(filter(is_affordable,products))
print(is_affordable)
print(is_affordable[1]["name"]+ str(is_affordable[1]["price"]))
print(is_affordable[3]["name"]+ str(is_affordable[3]["price"]))
# product is a list, so position is defined here



