""" (c)Heller """

from itertools import zip_longest

# Очень примитивная реализация
class Number:
        def __init__(self, registers):
                self.registers = []
                for x in registers:
                        if x > 255: raise ValueError("Register value more than 255")
                        self.registers.append(x)

        def __add__(self, other):
                overflow = False
                result = []
                for x, y in zip_longest(self.registers, other.registers, fillvalue = 0):
                        r = x + y
                        if overflow:
                                r += 1
                                overflow = False
                        if r > 255:
                                r -= 256
                                overflow = True
                        result.append(r)
                if overflow: result.append(1)
                return Number(result)


x = Number((2, 3))
y = Number((3, 255))
z = x + y
print(z.registers)
