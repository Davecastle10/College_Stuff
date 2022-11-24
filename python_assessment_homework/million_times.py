import time
import random
def megaflop_timer():

    start = time.time()
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    total = 0
    for i in range(1000000):
        total = total + (x * y)


    end = time.time()
    print(end-start, "secconds")

megaflop_timer()