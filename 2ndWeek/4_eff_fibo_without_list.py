def fibo(n):
    i = 0               # первое число Фибоначчи
    j = 1               # второе число Фибоначчи
    count = 2
    while count != n:
        sum_i_j = i + j # в эту переменную будет записываться конечный результат
        i = j
        j = sum_i_j
        count += 1
    return sum_i_j
