def not_so_bad_fibo(n): #(c)Heller
    """Calculating Fibonacci numbers more effectively than recursively"""
    if n == 0 or n == 1: return n
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b

def strings_without_11(n):
    """Calculating how much strings (len(n)) without two ones in a row"""
    return not_so_bad_fibo(n+2)


