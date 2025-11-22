from typing import List

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s: List[int] = [1, 2, 2]
        count = 1  # number of '1's counted so far in s
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]  # flip between 1 and 2
            for _ in range(s[index]):
                s.append(next_num)
            if next_num == 1:
                count += s[index]
            index += 1

        if len(s) > n:
            # remove the excess count of '1's beyond length n
            excess = len(s) - n
            if s[-1] == 1:
                count -= excess

        return count