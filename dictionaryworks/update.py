#update dictionary value

product={"id":100,"title":"goodday","price":35,}

product["exp.date"]="11-12-2024"

print(product)

product["offer"]=20

print(product)

# add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)