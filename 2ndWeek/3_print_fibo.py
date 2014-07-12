def fibo(n):
    print("Начинаю вычислять чиcло Фибоначчи до " + str(n))
    if n == 0: return 0
    if n == 1: return 1
    else: result = fibo(n - 1) + fibo(n - 2) # так как тут идут две ветки, вывод будет очень непонятным
    print("Вычислил до " + str(n) + " = " + str(result)) 
    return result
