def is_number(x):
    """Функция будет проверять является ли строка x числом"""
    try:                # Пробуем привести данную строку x к числу с точкой
        x = float(x)    
        return True     # Если получилось
    except ValueError:
        return False    # Если выдает ошибку значения, которое нельзя представить в виде числа с точкой

print(is_number('468947'))
print(is_number("I'm an integer"))

while True:
    something = input('Enter something\n')
    print(is_number(something))
    if something == 'stop':
        break


    #if x.isdigit() == True:    # Не подходит, потому что
    #    return True            # isdigit проверяет только цифры,
    #else:                      # а не числа. на отрицательных или
    #    return False           # не целых числах выдает False
