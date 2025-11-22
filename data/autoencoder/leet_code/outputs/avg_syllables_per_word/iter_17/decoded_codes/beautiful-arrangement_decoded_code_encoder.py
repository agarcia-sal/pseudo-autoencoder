class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(used_list, current_index):
            if current_index == n + 1:
                return 1
            count = 0
            for i in range(1, n + 1):
                if not used_list[i] and (i % current_index == 0 or current_index % i == 0):
                    used_list[i] = True
                    count += backtrack(used_list, current_index + 1)
                    used_list[i] = False
            return count

        used_list = [False] * (n + 1)
        return backtrack(used_list, 1)