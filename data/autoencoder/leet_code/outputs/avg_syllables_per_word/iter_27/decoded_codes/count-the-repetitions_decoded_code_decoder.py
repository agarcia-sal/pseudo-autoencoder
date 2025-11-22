from typing import List

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        len_s2 = len(s2)
        # s2_count[i]: how many times s2 is matched after scanning s1 i times
        s2_count: List[int] = [0] * (n1 + 1)
        # index_map[i]: current index in s2 after scanning s1 i times
        index_map: List[int] = [0] * (n1 + 1)

        current_index_s2 = 0  # index in s2 currently to match
        s1_count = 0

        while s1_count < n1:
            s1_count += 1
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

            # Check if current_index_s2 appeared before in index_map[1..s1_count-1]
            prev_occurrences = index_map[1:s1_count]
            if current_index_s2 in prev_occurrences:
                start = prev_occurrences.index(current_index_s2) + 1  # position in index_map where cycle starts (1-based)
                cycle_length = s1_count - start
                # Number of full cycles we can fit into remaining s1 scans after start
                cycles_fit = (n1 - start) // cycle_length
                remainder = (n1 - start) % cycle_length

                total_s2_count = (
                    s2_count[start]
                    + cycles_fit * (s2_count[start + cycle_length] - s2_count[start])
                    + (s2_count[start + remainder] - s2_count[start])
                )
                return total_s2_count // n2

        return s2_count[n1] // n2