class Solution:
    def largestVariance(self, s: str) -> int:
        def calculate_variance(substring: str, a: str, b: str) -> int:
            max_variance = 0
            count_a = 0
            count_b = 0
            has_b = False
            first_b = False

            for char in substring:
                if char == a:
                    count_a += 1
                elif char == b:
                    count_b += 1
                    has_b = True

                if count_b > 0:
                    max_variance = max(max_variance, count_a - count_b)
                elif first_b:
                    max_variance = max(max_variance, count_a - 1)

                if count_b > count_a:
                    count_a = 0
                    count_b = 0
                    first_b = has_b
            return max_variance

        max_variance = 0
        unique_chars = set(s)
        for char_a in unique_chars:
            for char_b in unique_chars:
                if char_a == char_b:
                    continue
                max_variance = max(max_variance, calculate_variance(s, char_a, char_b))

        return max_variance