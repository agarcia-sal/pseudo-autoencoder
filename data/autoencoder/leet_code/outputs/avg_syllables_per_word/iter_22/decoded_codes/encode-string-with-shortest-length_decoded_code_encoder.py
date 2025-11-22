class Solution:
    def encode(self, s: str) -> str:
        def get_encoded_length(count: int, substring: str) -> int:
            # Length of the encoding "count[substring]"
            return len(str(count)) + len(substring) + 2

        def dp(i: int, j: int) -> str:
            substring = s[i : j + 1]
            n = j - i + 1
            if n < 5:
                return substring

            shortest = substring
            # Check if substring consists of repeated patterns
            for k in range(1, n // 2 + 1):
                if n % k == 0:
                    repeat_count = n // k
                    pattern = substring[0:k]
                    if pattern * repeat_count == substring:
                        encoded_candidate = str(repeat_count) + '[' + dp(i, i + k - 1) + ']'
                        if len(encoded_candidate) < len(shortest):
                            shortest = encoded_candidate

            # Try breaking the substring into two parts and encode them separately
            for k in range(i, j):
                left_encoded = dp(i, k)
                right_encoded = dp(k + 1, j)
                combined = left_encoded + right_encoded
                if len(combined) < len(shortest):
                    shortest = combined

            return shortest

        return dp(0, len(s) - 1)