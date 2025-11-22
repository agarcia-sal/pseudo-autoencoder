from math import factorial

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact
        permutation_string = ''.join(result)
        return permutation_string