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
            times = s[index]
            s.extend([next_num] * times)
            if next_num == 1:
                count += times
            index += 1

        if len(s) > n:
            count -= (len(s) - n) * (1 if s[-1] == 1 else 0)

        return count