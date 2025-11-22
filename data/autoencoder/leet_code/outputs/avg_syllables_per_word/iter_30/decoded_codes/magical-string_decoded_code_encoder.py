class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        s = [1, 2, 2]
        count = 1  # count of ones in s
        index = 2
        while len(s) < n:
            next_num = 3 - s[-1]  # toggles between 1 and 2
            s.extend([next_num] * s[index])
            if next_num == 1:
                count += s[index]
            index += 1
        if len(s) > n:
            count -= s[-1] * (len(s) - n)
        return count