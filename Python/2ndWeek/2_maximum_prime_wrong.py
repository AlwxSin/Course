# Напишите функцию maximum_prime(n),
# Которая принимает на вход какое-то натуральное число,
# А возвращает в качестве результата его наибольший простой множитель.

def maximum_prime(n):
    n = int(n)
    if n == 1:
        return print("1 is not a prime")
    if n == 2:
        return n                                # Т.к. для двойки наибольший простой множитель будет двойка
    if n >= 3:
        min_prime = 3                           # Минимальное простое число для вычисления
        prime_numbers = []                      # Список в который будут писаться все множители n
        while n >= min_prime:
            if n % min_prime == 0:
                prime_numbers.append(min_prime) # Записываем по одному все найденые простые множители
                n = n / min_prime
            else:
                min_prime += 2                  # Переход к следующему возможному простому множителю
        return max(prime_numbers)
                
