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
            s.extend([next_num] * s[index])
            if next_num == 1:
                count += s[index]
            index += 1

        if len(s) > n:
            excess = len(s) - n
            # subtract the excess count of last appended number if it's '1'
            if s[-1] == 1:
                count -= excess

        return count