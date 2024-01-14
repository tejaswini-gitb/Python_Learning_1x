# 2

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

def is_affordable(abc):
    return abc["price"] < 500
def is_affordable_name(abc):
    return len(abc["name"]) < 5

affordable_items=tuple(filter(is_affordable,products))
for i in  affordable_items:
    print(i["price"],i["name"])
affordable_items_name=list(filter(is_affordable_name,products))
for i in  affordable_items_name:
    print(i["price"],i["name"])
