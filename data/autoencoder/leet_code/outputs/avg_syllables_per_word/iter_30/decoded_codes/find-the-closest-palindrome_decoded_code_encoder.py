class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()
        # Edge palindromes like 10^length + 1 and 10^(length-1) - 1
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        prefix = int(n[: (length + 1) // 2])
        for i in (-1, 0, 1):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]

            candidates.add(int(candidate))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(candidates, key=lambda x: (abs(x - original_number), x))
        return str(closest)