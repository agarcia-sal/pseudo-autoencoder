class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(used_collection, index):
            if index == n + 1:
                return 1
            count = 0
            for i in range(1, n + 1):
                if not used_collection[i] and (i % index == 0 or index % i == 0):
                    used_collection[i] = True
                    count += backtrack(used_collection, index + 1)
                    used_collection[i] = False
            return count

        used_collection = [False] * (n + 1)
        return backtrack(used_collection, 1)