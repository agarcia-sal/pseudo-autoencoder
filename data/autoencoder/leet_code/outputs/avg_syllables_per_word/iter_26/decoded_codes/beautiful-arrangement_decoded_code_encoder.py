class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(used_list, current_position):
            if current_position == n + 1:
                return 1

            arrangement_count = 0
            for candidate in range(1, n + 1):
                if not used_list[candidate] and (candidate % current_position == 0 or current_position % candidate == 0):
                    used_list[candidate] = True
                    arrangement_count += backtrack(used_list, current_position + 1)
                    used_list[candidate] = False
            return arrangement_count

        used_list = [False] * (n + 1)
        return backtrack(used_list, 1)