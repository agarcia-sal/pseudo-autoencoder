class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(used_collection: list[bool], index_value: int) -> int:
            if index_value == n + 1:
                return 1
            count_value = 0
            for i_value in range(1, n + 1):
                if not used_collection[i_value] and (i_value % index_value == 0 or index_value % i_value == 0):
                    used_collection[i_value] = True
                    count_value += backtrack(used_collection, index_value + 1)
                    used_collection[i_value] = False
            return count_value

        used_collection = [False] * (n + 1)
        return backtrack(used_collection, 1)