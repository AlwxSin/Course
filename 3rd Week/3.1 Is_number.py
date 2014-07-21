def is_number(x):
    """Функция будет проверять является ли строка x числом"""
    if x.isdigit() == True:
        return True
    else:
        return False

print(is_number('468947'))
print(is_number("I'm an integer"))
