from time import sleep
def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.2)
    print()
x = 1 
while x < 1000:
    print_slow(x)
    if x == 100:
     break
    x += 1

   