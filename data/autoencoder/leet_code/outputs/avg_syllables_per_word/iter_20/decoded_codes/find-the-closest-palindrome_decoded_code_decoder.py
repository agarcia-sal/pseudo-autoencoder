class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()

        candidates.add(10**(length+1) + 1)  # e.g. 100...001 for length+1 digits
        candidates.add(10**(length-1) - 1)  # e.g. 999...999 for length-1 digits

        prefix = int(n[: (length + 1) // 2])

        for i in (-1, 0, 1):
            new_prefix_str = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix_str + new_prefix_str[::-1]
            else:
                candidate = new_prefix_str + new_prefix_str[-2::-1]
            candidates.add(int(candidate))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(
            candidates,
            key=lambda x: (abs(x - original_number), x)
        )

        return str(closest)