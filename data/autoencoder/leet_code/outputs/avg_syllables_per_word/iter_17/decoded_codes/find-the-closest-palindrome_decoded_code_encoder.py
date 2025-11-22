class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()

        # Add 10^(length) + 1 and 10^(length - 1) - 1 to candidates
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        prefix = int(n[: (length + 1) // 2])
        for i in range(-1, 2):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                # even length: mirror whole prefix reversed
                candidate = new_prefix + new_prefix[::-1]
            else:
                # odd length: mirror prefix without last char reversed
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(int(candidate))

        original_number = int(n)
        if original_number in candidates:
            candidates.remove(original_number)

        # Find the closest palindrome by absolute difference, then value
        closest = min(
            candidates,
            key=lambda x: (abs(x - original_number), x)
        )

        return str(closest)