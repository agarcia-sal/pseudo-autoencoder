from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len_s1])

        if count_s1 == count_s2:
            return True

        for i in range(len_s1, len_s2):
            count_s2[s2[i]] += 1
            count_s2[s2[i - len_s1]] -= 1

            if count_s2[s2[i - len_s1]] == 0:
                del count_s2[s2[i - len_s1]]

            if count_s1 == count_s2:
                return True

        return False