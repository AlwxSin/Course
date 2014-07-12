import time

def fibo1(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo1(n - 1) + fibo1(n - 2)

def fibo2(n):
    numbers = [0, 1]
    while len(numbers) != n:
        numbers.append(numbers[-1] + numbers[-2])
    return max(numbers)

def compare_functions(f, g, n):
    i = 0
    t1 = 0
    t2 = 0
    while i < 1000:
        last_time = time.clock()
        f(n)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(n)
        t2 += time.clock() - last_time
        i += 1
    print(round(t1, 4), round(t2, 4), round((t2 / t1), 4))

# допустим fibo1 и fibo2 - это две функции
# вычисляющие значения чисел Фибоначчи,
# но разными методами
# compare_functions(fibo1, fibo2, 50)
# после этого вызова на экран будет выведено
# во сколько раз вторая функция работает быстрее
# или медленнее первой
