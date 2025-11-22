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
                    # else s2_count[s1_count] remains s2_count[s1_count - 1]
                # update index_map at the end of each character of s1
                index_map[s1_count] = current_index_s2
            else:
                # If no full cycle completed in this iteration,
                # we should propagate the previous count forward
                if s2_count[s1_count] == 0:
                    s2_count[s1_count] = s2_count[s1_count - 1]

            # Check if current_index_s2 appeared before to find cycles
            if current_index_s2 in index_map[:s1_count]:
                start = index_map.index(current_index_s2)
                cycle_length = s1_count - start
                cycles_fit = (n1 - start) // cycle_length
                remainder = (n1 - start) % cycle_length

                total_s2_count = s2_count[start] + \
                                 cycles_fit * (s2_count[start + cycle_length] - s2_count[start]) + \
                                 (s2_count[start + remainder] - s2_count[start])

                return total_s2_count // n2

        return s2_count[n1] // n2