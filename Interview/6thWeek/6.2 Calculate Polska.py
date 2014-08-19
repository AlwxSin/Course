def is_number(x):
    """Функция будет проверять является ли строка x числом"""
    # Из заданий по Питону
    try:                # Пробуем привести данную строку x к числу с точкой
        x = float(x)    
        return True     # Если получилось
    except ValueError:
        return False    # Если выдает ошибку значения, которое нельзя представить в виде числа с точкой

def calculate(polska):
    """ Вычисляет обратную польскую запись """
    buffer = []
    for x in polska:
        if is_number(x):
            buffer.append(x)
        else:
            current_number = buffer.pop(-2)
            if x == '+':
               current_number += buffer.pop(-1)
            elif x == '-':
               current_number -= buffer.pop(-1)
            elif x == '*':
               current_number *= buffer.pop(-1)
            elif x == '/':
               current_number /= buffer.pop(-1)
            else:
               raise ValueError('What is - "' + str(x) + '"?\nI can\'t handle this. Give me new list')
            buffer.append(current_number)
    return buffer[0]

#print(calculate([2, 3, '+', 4,3,'*',6,'/','-']))    # 3
#print(calculate([7,1,2,'*',4,2,'/','-','+']))       # 7
#print(calculate([3,5,7,5,10,'+','+','+','+']))      # 30
#print(calculate([3,5,7,5,10,'+','+','+','d']))      # error
