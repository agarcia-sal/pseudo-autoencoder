class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            # For single digit n, just return n-1 as string
            return str(int(n) - 1)

        candidates = set()

        # Edge candidates: 10^(length) + 1 and 10^(length - 1) - 1
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        for i in (-1, 0, 1):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                # Even length: palindrome = new_prefix + reversed new_prefix
                candidate = new_prefix + new_prefix[::-1]
            else:
                # Odd length: palindrome = new_prefix + reversed new_prefix except last char
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(int(candidate))

        original_number = int(n)
        candidates.discard(original_number)

        # Find closest palindrome by abs difference, break ties with smaller palindrome
        closest = min(candidates, key=lambda x: (abs(x - original_number), x))
        return str(closest)