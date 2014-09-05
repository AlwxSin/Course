def longest_palindrome(palindrome):
    palindromes = [] # Сюда записать все палиндромы в строке
    for i in range(len(palindrome)):
        for j in range(i, len(palindrome)):
            if palindrome[i:j] == palindrome [j:i:-1]:
                palindromes.append(palindrome[i:j+1])
    result = [] # Здесь только самый(самые) длинные палиндромы
    palindromes.sort(key = len)
    result.append(palindromes.pop(-1))
    while len(result[0]) == len(palindromes[-1]):
        result.append(palindromes.pop(-1))
    result = set(result)
    return result

