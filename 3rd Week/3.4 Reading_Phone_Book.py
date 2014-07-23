def phone_dict():
    '''Making a dict from a file'''
    s = open('phone_book.txt')
    string =()                      # Read line by line in to the variable
    phones = {}                     # Dictionary - goal
    while True:
        string = s.readline()
        if string == '': break      # At the end of the file - break
        else:
            string = string.strip('\n')                                             # Deleting '\n' at the end of each string
            key, phones[key] = string.rsplit('-',1)[0], string.rsplit('-',1)[1]     # Making a dict
    s.close()
    return phones

def phone_tuple():
    '''Making a list of tuples from a file'''
    s = open('phone_book.txt')
    string = ()
    phones = []
    while True:
        string = s.readline()
        if string == '': break
        else:
            string = string.strip('\n')
            phones.append(tuple(string.rsplit('-',1)))                              # Instead of dict making a tuples inside a list
    s.close()
    return phones

def phone_tuple_sort():
    '''Making a list of sorted tuples from a file'''
    s = open('phone_book.txt')
    string = ()
    phones = []
    while True:
        string = s.readline()
        if string == '': break
        else:
            string = string.strip('\n')
            phones.append(tuple(string.rsplit('-',1)))
    s.close()
    return sorted(phones)   # Sorted tuples inside a list
