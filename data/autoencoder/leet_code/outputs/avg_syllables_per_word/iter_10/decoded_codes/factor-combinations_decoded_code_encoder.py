from math import isqrt

class Solution:
    def getFactors(self, n):
        result = []
        path = []

        def backtrack(start, target):
            for i in range(start, isqrt(target) + 1):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        backtrack(2, n)
        return result