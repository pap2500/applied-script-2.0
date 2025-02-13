import random

print("1 - sten")
print("2 - sax")
print("3 - påse")

val = input("skriv ditt val\n")

valt_nummer = int(val)

data_val = random.randint(1,3)
print("datorn valde" + str(data_val))

if valt_nummer == data_val:
    print("det blir lika")
elif valt_nummer == 1:
    if data_val == 2:
         print("du vann")
else:
    print("du förlorade")
