# First try
'''
def reverse(x):
    """ Принимает список, возвращает перевернутый список"""
    result = []
    for i in x:
        result.insert(0,i)
    return result
'''

x1 = [0,1,2,3,4,5,6,7,8,9]
x2 = ['a','b','c','d','e','f','g','h','i','g']

#Second try
def reverse(x):
    lenght = len(x)
    for i in range(lenght-1, -1, -1):
        x.append(x[i])
    return x[lenght:]
    




print(reverse(x1))
print(reverse(x2))


