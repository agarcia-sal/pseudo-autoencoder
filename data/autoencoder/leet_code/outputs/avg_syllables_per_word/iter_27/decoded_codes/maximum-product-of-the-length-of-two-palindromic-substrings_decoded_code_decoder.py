from typing import List

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_len_end = [1] * n
        max_len_start = [1] * n

        def expand_around_center(left: int, right: int) -> None:
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if length > max_len_end[right]:
                    max_len_end[right] = length
                if length > max_len_start[left]:
                    max_len_start[left] = length
                left -= 1
                right += 1

        for i in range(n):
            expand_around_center(i, i)

        prefix_max = [0] * n
        suffix_max = [0] * n

        prefix_max[0] = max_len_end[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], max_len_end[i])

        suffix_max[-1] = max_len_start[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], max_len_start[i])

        max_product = 0
        for i in range(n - 1):
            potential_product = prefix_max[i] * suffix_max[i + 1]
            if potential_product > max_product:
                max_product = potential_product

        return max_product