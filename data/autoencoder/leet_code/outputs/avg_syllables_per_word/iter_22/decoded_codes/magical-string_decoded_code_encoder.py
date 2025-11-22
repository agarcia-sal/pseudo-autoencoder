class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1  # count of '1's
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]
            repetitions = s[index]
            s.extend([next_num] * repetitions)
            if next_num == 1:
                count += repetitions
            index += 1

        if len(s) > n:
            excess = len(s) - n
            count -= s[-1] * excess

        return count