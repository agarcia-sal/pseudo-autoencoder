import math
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start: int, target: int):
            for i in range(start, int(math.isqrt(target)) + 1):
                if target % i == 0:
                    # Append current factor combination to result ([...path, i, target//i])
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        result = []
        path = []
        backtrack(2, n)
        return result