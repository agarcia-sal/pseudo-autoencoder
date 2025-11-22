from math import sqrt, floor

def getFactors(n):
    result = []
    path = []

    def backtrack(start, target):
        for i in range(start, floor(sqrt(target)) + 1):
            if target % i == 0:
                result.append(path + [i, target // i])
                path.append(i)
                backtrack(i, target // i)
                path.pop()

    backtrack(2, n)
    return result