# 1


products=[
    {"name" : "laptop", "price" : 10000},
    {"name" : "pen", "price" : 2000},
    {"name" : "bag", "price" : 500},
    {"name" : "wire", "price" : 800},
    {"name" : "sheet", "price" : 100},
    {"name" : "headphone", "price" : 400},
    {"name" : "phone", "price" : 1000},
]

print(products)
print(type(products))   # list
print(type(products[1]))  # dict

def is_affordable(items):
    return items["price"] > 200

is_affordable=list(filter(is_affordable,products))
print(is_affordable)
print(is_affordable[1]["name"]+ str(is_affordable[1]["price"]))
print(is_affordable[3]["name"]+ str(is_affordable[3]["price"]))
# product is a list, so position is defined here



