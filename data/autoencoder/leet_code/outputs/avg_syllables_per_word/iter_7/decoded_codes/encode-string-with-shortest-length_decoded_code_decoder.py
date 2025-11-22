from typing import Dict, Tuple

class Solution:
    def encode(self, s: str) -> str:
        memo: Dict[Tuple[int, int], str] = {}

        def dp(i: int, j: int) -> str:
            if (i, j) in memo:
                return memo[(i, j)]

            substring = s[i : j + 1]
            n = j - i + 1
            if n < 5:
                memo[(i, j)] = substring
                return substring

            shortest = substring
            for k in range(1, n // 2 + 1):
                if n % k == 0:
                    repeat_count = n // k
                    pattern = substring[:k]
                    if pattern * repeat_count == substring:
                        encoded_candidate = f"{repeat_count}[{dp(i, i + k - 1)}]"
                        if len(encoded_candidate) < len(shortest):
                            shortest = encoded_candidate

            for k in range(i, j):
                left_encoded = dp(i, k)
                right_encoded = dp(k + 1, j)
                combined = left_encoded + right_encoded
                if len(combined) < len(shortest):
                    shortest = combined

            memo[(i, j)] = shortest
            return shortest

        return dp(0, len(s) - 1)