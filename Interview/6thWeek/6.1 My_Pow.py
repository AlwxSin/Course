def my_pow(x, n):
    """ Возведения числа x в степень n """
    if n == 0:
        return 1
    if n % 2 == 1:
        return my_pow(x, n-1) * x
    else:
        res = my_pow(x, n/2)
        return res * res
