from math import factorial
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers: List[int] = list(range(1, n + 1))
        k -= 1
        result: List[str] = []
        for i in range(n, 0, -1):
            fact: int = factorial(i - 1)
            index: int = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact
        permutation_string: str = ''.join(result)
        return permutation_string