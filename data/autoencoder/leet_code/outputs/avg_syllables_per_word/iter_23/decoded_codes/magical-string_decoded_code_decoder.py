from typing import List

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s: List[int] = [1, 2, 2]
        count = 1
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]
            repeats = s[index]
            s.extend([next_num] * repeats)
            if next_num == 1:
                count += repeats
            index += 1

        if len(s) > n:
            extra_length = len(s) - n
            last_element = s[-1]
            count -= last_element * extra_length

        return count