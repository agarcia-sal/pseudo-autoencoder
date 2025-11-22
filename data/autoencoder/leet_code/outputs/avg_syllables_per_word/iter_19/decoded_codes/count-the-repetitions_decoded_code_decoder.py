from typing import List

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        s2_count: List[int] = [0] * (n1 + 1)
        index_map: List[int] = [0] * (n1 + 1)

        current_index_s2 = 0
        s1_count = 0

        while s1_count < n1:
            s1_count += 1
            for ch in s1:
                if ch == s2[current_index_s2]:
                    current_index_s2 += 1
                    if current_index_s2 == len(s2):
                        s2_count[s1_count] = s2_count[s1_count - 1] + 1
                        current_index_s2 = 0
                # update index_map for current s1_count iteration to the latest current_index_s2
                index_map[s1_count] = current_index_s2

            # check if a previous occurrence of current_index_s2 exists to detect a cycle
            for start in range(s1_count):
                if index_map[start] == current_index_s2:
                    cycle_length = s1_count - start
                    cycles_fit = (n1 - start) // cycle_length
                    remainder = (n1 - start) % cycle_length

                    total_s2_count = (
                        s2_count[start]
                        + cycles_fit * (s2_count[start + cycle_length] - s2_count[start])
                        + s2_count[start + remainder] - s2_count[start]
                    )
                    return total_s2_count // n2

        return s2_count[s1_count] // n2