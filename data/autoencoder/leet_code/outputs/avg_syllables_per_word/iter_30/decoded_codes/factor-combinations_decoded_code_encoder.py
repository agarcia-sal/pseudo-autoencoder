from math import isqrt

class Solution:
    def getFactors(self, n):
        def backtrack(start, target):
            for i in range(start, isqrt(target) + 1):
                if target % i == 0:
                    # append current path + [i, target//i] to result
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        result = []
        path = []
        backtrack(2, n)
        return result