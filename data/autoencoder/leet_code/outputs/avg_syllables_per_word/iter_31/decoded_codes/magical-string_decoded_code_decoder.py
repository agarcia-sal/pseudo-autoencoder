from typing import List

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s: List[int] = [1, 2, 2]
        count = 1  # count of ones
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]
            for _ in range(s[index]):
                s.append(next_num)
            if next_num == 1:
                count += s[index]
            index += 1

        if len(s) > n:
            extra_length = len(s) - n
            count -= s[-1] * extra_length

        return count