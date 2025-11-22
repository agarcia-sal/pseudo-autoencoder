from typing import List

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        len_s2 = len(s2)
        s2_count: List[int] = [0] * (n1 + 1)
        index_map: List[int] = [0] * (n1 + 1)
        current_index_s2 = 0

        for s1_count in range(1, n1 + 1):
            for char in s1:
                if char == s2[current_index_s2]:
                    current_index_s2 += 1
                    if current_index_s2 == len_s2:
                        s2_count[s1_count] = s2_count[s1_count - 1] + 1
                        current_index_s2 = 0
                    else:
                        s2_count[s1_count] = s2_count[s1_count - 1]
                else:
                    s2_count[s1_count] = s2_count[s1_count - 1]
                index_map[s1_count] = current_index_s2

            # Check if current_index_s2 appeared previously in index_map[0..s1_count-1]
            # If yes, it means a cycle is detected
            # We find the start of the cycle and use it to compute the result quickly
            for start in range(s1_count):
                if index_map[start] == current_index_s2:
                    cycle_length = s1_count - start
                    remaining = n1 - start
                    cycles_fit = remaining // cycle_length
                    remainder = remaining % cycle_length

                    total_s2_count = (
                        s2_count[start]
                        + cycles_fit * (s2_count[start + cycle_length] - s2_count[start])
                        + (s2_count[start + remainder] - s2_count[start])
                    )
                    return total_s2_count // n2

        return s2_count[n1] // n2