class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            original_number = int(n)
            result = original_number - 1
            return str(result)

        candidates = set()
        candidates.add(10 ** (length + 1))               # e.g. 1000 for length=3
        candidates.add(10 ** (length - 1) - 1)           # e.g. 99 for length=3

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        for i in range(-1, 2):
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                # even length: mirror entire new_prefix
                candidate = new_prefix + new_prefix[::-1]
            else:
                # odd length: mirror all except last char of new_prefix
                candidate = new_prefix + new_prefix[:-1][::-1]

            candidates.add(int(candidate))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(candidates, key=lambda x: (abs(x - original_number), x))
        return str(closest)