class Solution:
    def encode(self, s: str) -> str:
        def get_encoded_length(count: int, substring: str) -> int:
            # length of count as string + length of substring + 2 for brackets
            return len(str(count)) + len(substring) + 2

        n = len(s)
        # dp cache to avoid recomputation
        dp_cache = {}

        def dp(i: int, j: int) -> str:
            if (i, j) in dp_cache:
                return dp_cache[(i, j)]

            substring = s[i:j + 1]
            length = j - i + 1

            if length < 5:
                dp_cache[(i, j)] = substring
                return substring

            shortest = substring

            # Check if substring is composed of repeated pattern
            for k in range(1, length // 2 + 1):
                if length % k == 0:
                    repeat_count = length // k
                    repeated_pattern = substring[0:k] * repeat_count
                    if repeated_pattern == substring:
                        encoded_candidate = str(repeat_count) + '[' + dp(i, i + k - 1) + ']'
                        if len(encoded_candidate) < len(shortest):
                            shortest = encoded_candidate

            # Try every possible split
            for k in range(i, j):
                left_encoded = dp(i, k)
                right_encoded = dp(k + 1, j)
                combined = left_encoded + right_encoded
                if len(combined) < len(shortest):
                    shortest = combined

            dp_cache[(i, j)] = shortest
            return shortest

        return dp(0, n - 1) if n > 0 else ""