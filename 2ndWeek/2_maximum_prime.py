# Напишите функцию maximum_prime(n),
# Которая принимает на вход какое-то натуральное число,
# А возвращает в качестве результата его наибольший простой множитель.

# Нужна функция для определения простое ли число

def isprime(m):
    if m == 2:                                  # Исключаем 2
        return True
    if m < 2 or m % 2 == 0:                     # Исключаем 1 и все, что делится на 2
        return False
    for i in range(3, int(m ** 0.5) + 1, 2):    # Нужно перебрать числа, не превосходящие корня от искомого
        if m % i == 0:
            return False
    return True

# Теперь фунция нахождения наибольшего простого множителя

def maximum_prime(n):
    if isprime(n) == True:
        return n
    if n == 1:
        return print("1 is not a Prime")
    if n >= 2:
        for i in range(2, int(n)):        # Перебираем возможные множители
            if isprime(i) == True and n % i == 0:
                x = i                     # Записываем множитель в переменную  
        return x
