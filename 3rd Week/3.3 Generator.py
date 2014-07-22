from random import randint
import time

def generator(number_count):
    number_list = []
    start = time.clock()
    while len(number_list) != number_count:
        y = randint(1000000, 10000000)
        if y in number_list: continue
        else:
            number_list.append(y)
    finish = time.clock()
    print(finish-start)
    return True #number_list
        
