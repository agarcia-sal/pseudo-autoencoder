from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_of_s1 = len(s1)
        length_of_s2 = len(s2)

        if length_of_s1 > length_of_s2:
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:length_of_s1])

        if count_s1 == count_s2:
            return True

        for index in range(length_of_s1, length_of_s2):
            count_s2[s2[index]] += 1
            char_to_remove = s2[index - length_of_s1]
            count_s2[char_to_remove] -= 1
            if count_s2[char_to_remove] == 0:
                del count_s2[char_to_remove]

            if count_s1 == count_s2:
                return True

        return False