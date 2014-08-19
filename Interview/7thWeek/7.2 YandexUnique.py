def unique_number(massive):
    d = {1: set(), 2: set()}    # В 1 записать числа, которые встречаются хотя бы раз
    for x in massive:           # В 2 хотя бы дважды
        if x not in d[1]:
            d[1].add(x)
        else:
            d[2].add(x)
    return d[1].difference(d[2]).pop()
