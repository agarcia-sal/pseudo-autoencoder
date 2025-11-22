from typing import List

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_len_end = [1] * n  # max palindrome length ending at i
        max_len_start = [1] * n  # max palindrome length starting at i

        def expand_around_center(left: int, right: int) -> None:
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if max_len_end[right] < length:
                    max_len_end[right] = length
                if max_len_start[left] < length:
                    max_len_start[left] = length
                left -= 1
                right += 1

        for i in range(n):
            # odd length palindromes
            expand_around_center(i, i)
            # even length palindromes
            if i + 1 < n:
                expand_around_center(i, i + 1)

        prefix_max = [0] * n
        prefix_max[0] = max_len_end[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], max_len_end[i])

        suffix_max = [0] * n
        suffix_max[-1] = max_len_start[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], max_len_start[i])

        max_product = 0
        for i in range(n - 1):
            product = prefix_max[i] * suffix_max[i + 1]
            if max_product < product:
                max_product = product

        return max_product