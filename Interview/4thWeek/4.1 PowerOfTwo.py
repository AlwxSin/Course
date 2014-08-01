def power_of_two(x):
    """Является ли число степенью двойки"""
    if x == 1: return True
    two = 2 << len(bin(x))-4
    return x == two
    


print(power_of_two(1))
print(power_of_two(7))
print(power_of_two(32))
print(power_of_two(128))
print(power_of_two(736))
