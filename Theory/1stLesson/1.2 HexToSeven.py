def chr_to_num(x):
    x = ord(x)
    if ord("0") <= x <= ord("9"): return x - ord("0")
    elif ord("a") <= x <= ord("z"): return x - ord("a") + 10
    else: return x - ord("A") + 10

def to_seven(x):
    """Returns a seven representation of a natural number"""
    if x == None:
        return False
    result = ""
    x = int(x)
    while x:
        result += str(x%7)
        x //= 7
    return result[::-1]

def hex_to_dec(x):
    """Returns a decimal representation of hex number"""
    result = 0
    grade = len(x)-1
    for i in x:
        if chr_to_num(i) > 15:
            return print('Not a hex')
        else:
            result += chr_to_num(i)*(16**grade)
            grade -= 1
    return str(result)

def hex_to_seven(x):
    x = hex_to_dec(x)   # First i need to see decimal
    x = to_seven(x)     # Now from decimal i can convert to seven
    return x

print(hex_to_seven('5'))
print(hex_to_seven('68645'))
print(hex_to_seven('68abcde45'))
print(hex_to_seven('686AbCa5'))
print(hex_to_seven('686hi45'))
