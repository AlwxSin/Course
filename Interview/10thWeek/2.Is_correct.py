def is_correct(string):
    if len(string) % 2 != 0:
        return False
    pairs = {
    "}": "{",
    "]": "[",
    ")": "(",}
    starts = []
    for s in string:
        if s in pairs.values():
            starts.append(s)
        elif s not in pairs:
            return False
        elif pairs[s] == starts[-1]:
            starts.pop()
    return len(starts) == 0

def unit_test():
    x = "[{}]()[()[]]"
    y = "[[}"
    z = "([)]"
    if is_correct(x) and not is_correct(y) and not is_correct(z):
        return True
    else:
        return False

