class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        for i, char in enumerate(s):
            character_index = ord(char) - ord('a')
            current_appeal += i - last[character_index]
            total_appeal += current_appeal
            last[character_index] = i
        return total_appeal