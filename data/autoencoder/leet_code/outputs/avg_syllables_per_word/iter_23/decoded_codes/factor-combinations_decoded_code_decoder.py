from math import isqrt
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start: int, target: int) -> None:
            for i in range(start, isqrt(target) + 1):
                if target % i == 0:
                    # Append a new list: path + [i, target // i]
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        result: List[List[int]] = []
        path: List[int] = []
        backtrack(2, n)
        return result