from functools import lru_cache

class Solution:
    def encode(self, s: str) -> str:

        def get_encoded_length(count: int, substring: str) -> int:
            return len(str(count)) + len(substring) + 2  # count + '[' + substring + ']'

        @lru_cache(None)
        def dp(i: int, j: int) -> str:
            substring = s[i:j+1]
            n = j - i + 1
            if n < 5:
                return substring

            shortest = substring

            # Try to encode by repeated patterns
            for k in range(1, n // 2 + 1):
                if n % k == 0:
                    repeat_count = n // k
                    pattern = substring[0:k]
                    if pattern * repeat_count == substring:
                        # encode the pattern itself recursively
                        encoded_pattern = dp(i, i + k - 1)
                        encoded_candidate = f"{repeat_count}[{encoded_pattern}]"
                        if len(encoded_candidate) < len(shortest):
                            shortest = encoded_candidate

            # Try all partitions to combine two encoded parts
            for k in range(i, j):
                left_encoded = dp(i, k)
                right_encoded = dp(k + 1, j)
                combined = left_encoded + right_encoded
                if len(combined) < len(shortest):
                    shortest = combined

            return shortest

        return dp(0, len(s) - 1)