class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()
        # 10^(length+1) + 1 is a palindrome of the form 100...001,
        # here just add 10^(length)+1 for the upper bound candidate
        candidates.add(10 ** (length - 1) - 1)  # Lower bound palindrome: 999...9 with length-1 digits
        candidates.add(10 ** length + 1)        # Upper bound palindrome: 100...001 with length+1 digits

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

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