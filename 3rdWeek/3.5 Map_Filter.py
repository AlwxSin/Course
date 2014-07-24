L = [x for x in range(-2, 16)] # Test list

def my_map(Func, arg):
    result = []
    for i in arg:
        result.append(Func(i))
    return result

def my_filter(Func, arg):
    result = []
    for i in arg:
        if Func(i) == True:
            result.append(i)
    return result

print(my_map(lambda x: x*2, L))
print(my_filter(lambda x: 2<x<15, L))
