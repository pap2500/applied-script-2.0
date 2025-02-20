import random
import time

spelar_namn = input("slå in ditt namn:")

spelar_val = random.randint(1,6)

data_val = random.randint(1,6)
time.sleep(3)
print("du", spelar_namn,"rullar:", spelar_val)
time.sleep(3)
print("datan rullar:",data_val)

if spelar_val > data_val:
    print("du", spelar_namn, "vinner" )
elif spelar_val == data_val:
    print("ovangjort det blir en ny runda")
else:
    print("du förlorar")