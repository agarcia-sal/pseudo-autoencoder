class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix_map = {0: -1}
        prefix_xor = 0
        max_length = 0

        for index, char in enumerate(s):
            digit = int(char)
            prefix_xor ^= 1 << digit

            if prefix_xor in prefix_map:
                max_length = max(max_length, index - prefix_map[prefix_xor])

            for bit_position in range(10):
                flipped = prefix_xor ^ (1 << bit_position)
                if flipped in prefix_map:
                    max_length = max(max_length, index - prefix_map[flipped])

            if prefix_xor not in prefix_map:
                prefix_map[prefix_xor] = index

        return max_length