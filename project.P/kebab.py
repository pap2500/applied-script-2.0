
import random
while True:
    print("Sten 1\nSax 2\nPåse 3\n")
    val = input("skriv ditt val\n")

    valt_nummer = int(val)





    data_val = random.randint(1,3)

    print("datan valde\n" + str(data_val))

    if valt_nummer > data_val:
        print("du vann")
    elif valt_nummer < data_val:
        print("du förlorar försök igen")
    elif valt_nummer == data_val:
        print("ovagjort försök igen")

    if valt_nummer > data_val:
        break
