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
                # Update index_map inside the for loop every character iteration,
                # but only the last written value per s1_count matters at the end of the s1 loop
                index_map[s1_count] = current_index_s2

            # Check if current_index_s2 appeared before in index_map[1..s1_count-1]
            # i.e., check for cycle start
            # We look in index_map from position 1 to s1_count-1 (inclusive)
            previously_found = None
            for i in range(1, s1_count):
                if index_map[i] == current_index_s2:
                    previously_found = i
                    break

            if previously_found is not None:
                start = previously_found
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