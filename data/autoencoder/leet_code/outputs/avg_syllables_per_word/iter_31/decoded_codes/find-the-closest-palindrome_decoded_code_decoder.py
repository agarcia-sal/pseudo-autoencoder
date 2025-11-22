from typing import Set

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates: Set[int] = set()
        # Edge cases: 10^length + 1 and 10^(length-1) - 1
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        prefix = int(n[: (length + 1) // 2])

        for i in (-1, 0, 1):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                # Even length: mirror the entire new_prefix reversed
                candidate = new_prefix + new_prefix[::-1]
            else:
                # Odd length: exclude the last character of new_prefix in the mirrored part
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(int(candidate))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(
            candidates,
            key=lambda x: (abs(x - original_number), x)
        )

        return str(closest)