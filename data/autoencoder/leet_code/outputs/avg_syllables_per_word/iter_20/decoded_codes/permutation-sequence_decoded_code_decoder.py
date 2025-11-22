from math import factorial
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers: List[int] = list(range(1, n + 1))
        k -= 1  # zero-based index
        result: List[str] = []
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(str(numbers[index]))
            del numbers[index]
            k %= fact
        return ''.join(result)