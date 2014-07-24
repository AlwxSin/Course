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
        phone_book[phone_numbers.pop()] = name_list.pop() # Making a dict Number: Name
    #finish = time.clock()
    #print(finish-start)
    return phone_book


# Writing in a file
phone_book = generator(100000)                              # Our phone book
file = open('phone_book.txt', 'w')                          # Making a new file
for key in phone_book:
    file.write(str(key) + '-' + phone_book[key] + '\n')   # Writing phone book in a file
file.close()

#test
#file = open('phone book.txt')
#listing = [line.strip() for line in file]
#print(listing)
#file.close()

# Reading from phone_book.txt
