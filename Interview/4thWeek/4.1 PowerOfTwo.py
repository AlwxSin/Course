def power_of_two(x):
    """Является ли число степенью двойки"""
    two = x&(x-1)
    return not two
    


print(power_of_two(1))  #True
print(power_of_two(2))  #True
print(power_of_two(7))  #False
print(power_of_two(32)) #True
print(power_of_two(128))#True
print(power_of_two(736))#False
