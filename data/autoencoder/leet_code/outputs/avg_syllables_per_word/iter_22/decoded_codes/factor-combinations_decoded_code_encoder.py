from math import isqrt
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int, target: int):
            limit = isqrt(target) + 1
            for i in range(start, limit):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        backtrack(2, n)
        return result