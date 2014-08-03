"""
В восьмеричной системе счисления используется восемь цифр от 0 до 7.
Напишите функцию, принимающую на вход строку в восьмеричной системе счисления,
и выдающую в качестве результата число (в обычном Питоновском смысле).
"""

def OctToDec(x):
    """Returns a decimal representation of a oct number"""
    #grade = len(x)-1
    result = 0
    for i in x:
        if int(i) > 7:
            return print('String must be in Octo')
        result *= 8
        result += int(i)
        #result += int(i)*(8**grade)
        #grade -= 1
    return result

print(OctToDec('5'))
print(OctToDec('0'))
print(OctToDec('45'))
print(OctToDec('453'))
print(OctToDec('4542'))
print(OctToDec('78315'))



"""
Ошибочный код. Сначала думал, что надо из Dec перевести в Oct.
result = ""
    if is_number(x) == True:
        if 0 <= int(x) <= 7:
            return x
        elif int(x) < 0:
            return print("Please, input a number above zero. I can't count negative numbers =(")
        else:
            while x:
                result += str(int(x)%8)
                x = int(x)//8
            return result[::-1]
    else:
        return print('x is not a number')
"""
