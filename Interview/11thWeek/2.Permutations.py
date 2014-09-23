def unit_test():
    result = permutations([1,2,3])
    answer = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    for i in answer:
        if i not in result:
            return False
    return len(result) == len(answer)

def permutations(array):
    if not array:
        return [[]]
    result = []
    for i in array:
        temp = array[:]
        temp.remove(i)
        result.extend([[i] + x for x in permutations(temp)])
    return result
