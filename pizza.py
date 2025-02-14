


from time import sleep

def print_slow(txt):
    for x in txt:
        print(x, end = '', flush=True)
        sleep(0.1)
    print()



spel_num = range(0,50)


for i in  range(spel_num):
    print_slow(i)
   