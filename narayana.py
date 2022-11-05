#TASK-1        
size=int(input("no.of products"))
products = []
for i in range(size):
    dictionary={}
    dictionary["price"]=int(input("Price:"))
    dictionary["name"]=input("Name:")
    dictionary["period"]=int(input("Period"))
    products.append(dictionary)

print(products)

#TASK-2

subs=input("substring : ")

res = [i for i in products if subs in i["name"]]
for j in res:
    print(j)

#TASK-3

periodl=int(input("low period : "))
periodh=int(input("high period : "))

pricel=int(input("low price : "))
priceh=int(input("high price : "))

for i in products:
    if ((i["price"]>=pricel and i["price"]<=priceh) or (i["period"]>=periodl and i["period"]<=periodh)):
        print(i)

#TASK-4

periodl=int(input("low period : "))
periodh=int(input("high period : "))

pricel=int(input("low price : "))
priceh=int(input("high price : "))

for i in products:
    if ((i["price"]>=pricel and i["price"]<=priceh) and (i["period"]>=periodl and i["period"]<=periodh)):
        print(i)

#TASK-5

name=input("name : ")
for i in products:
    if name==i["name"]:
        products.remove(i)
print(products)

#TASK-6

name2=input("name : ")
for i in products:
    if name2==i["name"]:
        i["price"]=int(input("updated price : "))
        i["period"]=int(input("updated period : "))

print(products)
