from math import isqrt
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int, target: int) -> None:
            limit = isqrt(target) + 1
            for i in range(start, limit):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        backtrack(2, n)
        return result