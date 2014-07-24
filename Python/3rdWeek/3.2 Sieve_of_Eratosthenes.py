def sieve(n):
    """ Функция возвращает список всех простых чисел до n используя решето Эратосфена"""
    numbers = []
    for i in range(2, n+1):
        numbers.append(i)                   # Список со всеми целыми от 2 до n
    p = 0                                   # Переменная с помощью которой исключаем ненужные элементы в списке
    count = 0
    while p != numbers[-1]:
        p = numbers[count]                  
        for i in range (p**2, n+1, p):      
            if i not in numbers:
                continue
            numbers.remove(i)
        count +=1        
    return numbers
