from math import isqrt
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start: int, target: int):
            for i in range(start, isqrt(target) + 1):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        result = []
        path = []
        backtrack(2, n)
        return result