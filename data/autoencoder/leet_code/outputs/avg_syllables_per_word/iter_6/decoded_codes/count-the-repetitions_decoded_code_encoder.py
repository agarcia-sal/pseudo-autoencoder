class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        l2 = len(s2)
        s2_count = [0] * (n1 + 1)
        index_map = [-1] * (l2 + 1)

        current_index_s2 = 0
        for s1_count in range(1, n1 + 1):
            for ch in s1:
                if ch == s2[current_index_s2]:
                    current_index_s2 += 1
                    if current_index_s2 == l2:
                        s2_count[s1_count] = s2_count[s1_count - 1] + 1
                        current_index_s2 = 0
                    else:
                        s2_count[s1_count] = s2_count[s1_count - 1]
                else:
                    s2_count[s1_count] = s2_count[s1_count - 1]
            if index_map[current_index_s2] != -1:
                start = index_map[current_index_s2]
                cycle_length = s1_count - start
                cycles_fit = (n1 - start) // cycle_length
                remainder = (n1 - start) % cycle_length
                total_s2_count = (
                    s2_count[start] +
                    cycles_fit * (s2_count[start + cycle_length] - s2_count[start]) +
                    (s2_count[start + remainder] - s2_count[start])
                )
                return total_s2_count // n2
            else:
                index_map[current_index_s2] = s1_count

        return s2_count[n1] // n2