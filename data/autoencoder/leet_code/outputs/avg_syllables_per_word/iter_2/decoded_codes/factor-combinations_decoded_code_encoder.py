class Solution:
    def getFactors(self, n):
        def backtrack(start, target):
            for i in range(start, int(target ** 0.5) + 1):
                if target % i == 0:
                    result.append(path + [i, target // i])
                    path.append(i)
                    backtrack(i, target // i)
                    path.pop()

        result = []
        path = []
        backtrack(2, n)
        return result