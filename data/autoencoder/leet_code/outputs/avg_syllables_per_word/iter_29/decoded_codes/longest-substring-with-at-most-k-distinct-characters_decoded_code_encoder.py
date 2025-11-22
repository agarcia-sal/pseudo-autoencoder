class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_to_pos = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            right_char = s[right]
            char_to_pos[right_char] = right

            if len(char_to_pos) > k:
                leftmost_char = min(char_to_pos, key=char_to_pos.get)
                left = char_to_pos[leftmost_char] + 1
                del char_to_pos[leftmost_char]

            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length

        return max_length