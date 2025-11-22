class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]
            repetition = s[index]
            s.extend([next_num] * repetition)

            if next_num == 1:
                count += repetition

            index += 1

        if len(s) > n:
            excess_length = len(s) - n
            last_element = s[-1]
            count -= last_element * excess_length

        return count