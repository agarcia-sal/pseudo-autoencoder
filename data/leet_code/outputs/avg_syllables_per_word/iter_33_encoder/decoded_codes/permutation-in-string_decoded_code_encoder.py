from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        count_s1 = Counter(s1)
        window_count = Counter(s2[:len_s1])

        if count_s1 == window_count:
            return True

        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]
            window_count[s2[i]] += 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]

            if window_count == count_s1:
                return True

        return False