from typing import Set


class Solution:
    def largestVariance(self, s: str) -> int:
        def calculate_variance(substring: str, char_a: str, char_b: str) -> int:
            max_variance = 0
            count_a = 0
            count_b = 0
            has_b = False
            first_b = False

            for ch in substring:
                if ch == char_a:
                    count_a += 1
                elif ch == char_b:
                    count_b += 1
                    has_b = True

                if count_b > 0:
                    max_variance = max(max_variance, count_a - count_b)
                elif count_b == 0 and first_b:
                    # If we've previously had b but count_b is zero now, consider count_a - 1
                    max_variance = max(max_variance, count_a - 1)

                if count_b > count_a:
                    # Reset counters and keep track whether we have had a b before
                    count_a = 0
                    count_b = 0
                    first_b = has_b

            return max_variance

        max_variance = 0
        unique_chars: Set[str] = set(s)

        for char_a in unique_chars:
            for char_b in unique_chars:
                if char_a == char_b:
                    continue
                max_variance = max(max_variance, calculate_variance(s, char_a, char_b))

        return max_variance