class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix_map = {0: -1}
        prefix_xor = 0
        max_length = 0
        for i, char in enumerate(s):
            digit = int(char)
            prefix_xor ^= 1 << digit
            if prefix_xor in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_xor])
            for j in range(10):
                flipped = prefix_xor ^ (1 << j)
                if flipped in prefix_map:
                    max_length = max(max_length, i - prefix_map[flipped])
            if prefix_xor not in prefix_map:
                prefix_map[prefix_xor] = i
        return max_length