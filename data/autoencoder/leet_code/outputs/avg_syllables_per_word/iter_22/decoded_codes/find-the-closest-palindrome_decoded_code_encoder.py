class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()
        # Edge candidates like 10^length + 1 and 10^(length-1) - 1
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        for i in range(prefix - 1, prefix + 2):
            new_prefix = str(i)
            if length % 2 == 0:
                # Even length: mirror entire prefix
                candidate_str = new_prefix + new_prefix[::-1]
            else:
                # Odd length: mirror all but last char of prefix
                candidate_str = new_prefix + new_prefix[:-1][::-1]
            candidates.add(int(candidate_str))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(candidates, key=lambda x: (abs(x - original_number), x))
        return str(closest)