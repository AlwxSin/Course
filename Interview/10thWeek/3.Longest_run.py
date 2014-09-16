def longest_run(array):
    array = set(array)
    array = list(array)
    array.sort()
    # К этому моменту список отсортирован и содержит только уникальные данные
    result = []
    tmp = []
    for i in range(len(array)):
        if tmp == []:
            tmp.append(array[i])
        elif array[i] == (tmp[-1] + 1):
            tmp.append(array[i])
        else:
            result.append(tmp)
            tmp = [array[i]]
    return max(result)
