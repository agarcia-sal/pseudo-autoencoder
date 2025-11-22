class Solution:
    def magicalString(self, n):
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1  # count of '1's so far
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]
            repeat_times = s[index]
            s.extend([next_num] * repeat_times)
            if next_num == 1:
                count += repeat_times
            index += 1

        if len(s) > n:
            excess = len(s) - n
            if s[-1] == 1:
                count -= excess

        return count