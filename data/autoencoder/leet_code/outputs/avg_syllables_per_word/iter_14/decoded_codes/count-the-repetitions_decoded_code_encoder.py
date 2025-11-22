class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        len_s2 = len(s2)
        s2_count = [0] * (n1 + 1)
        index_map = [0] * (n1 + 1)

        current_index_s2 = 0
        s1_count = 0

        while s1_count < n1:
            s1_count += 1
            for ch in s1:
                if ch == s2[current_index_s2]:
                    current_index_s2 += 1
                    if current_index_s2 == len_s2:
                        s2_count[s1_count] = s2_count[s1_count - 1] + 1
                        current_index_s2 = 0
                # Update index_map at position s1_count during iteration means after each char or after loop? 
                # Pseudocode sets at s1_count inside for loop, so overwrite repeatedly; the last overwrite stays
                index_map[s1_count] = current_index_s2

            # After processing one s1 segment, check if current_index_s2 appeared before to detect cycle
            found_cycle_start = -1
            for i in range(s1_count):
                if index_map[i] == current_index_s2:
                    found_cycle_start = i
                    break

            if found_cycle_start != -1:
                start = found_cycle_start
                cycle_len = s1_count - start
                cycles_fit = (n1 - start) // cycle_len
                remainder = (n1 - start) % cycle_len

                total_s2_count = (
                    s2_count[start]
                    + cycles_fit * (s2_count[start + cycle_len] - s2_count[start])
                    + (s2_count[start + remainder] - s2_count[start])
                )
                return total_s2_count // n2

        return s2_count[s1_count] // n2