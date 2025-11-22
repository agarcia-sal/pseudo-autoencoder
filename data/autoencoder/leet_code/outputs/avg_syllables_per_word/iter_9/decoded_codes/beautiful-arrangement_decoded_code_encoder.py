class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(used, index):
            if index == n + 1:
                return 1
            count = 0
            for i in range(1, n + 1):
                if not used[i] and (i % index == 0 or index % i == 0):
                    used[i] = True
                    count += backtrack(used, index + 1)
                    used[i] = False
            return count

        used = [False] * (n + 1)
        return backtrack(used, 1)