from random import randint, choice
from string import ascii_uppercase, ascii_lowercase
#import time

def generator(number_count):
    """Generates a dict Name: Number. Number of strings = number_count"""
    #start = time.clock()
    phone_numbers = set()
    name_list = set()
    phone_book = {}
    while len(phone_numbers) < number_count:
        phone_numbers.add(randint(100000, 10000000)) # Random unique 7-digit numbers
        name_list.add(str(choice(ascii_uppercase)) + str(''.join((choice(ascii_lowercase) for i in range(randint(4, 10)))))) # Random unique name, 4<len(name)<10
    for i in range(number_count):
        phone_book[name_list.pop()] = phone_numbers.pop() # Making a dict Name: Number
    #finish = time.clock()
    #print(finish-start)
    return phone_book
        
