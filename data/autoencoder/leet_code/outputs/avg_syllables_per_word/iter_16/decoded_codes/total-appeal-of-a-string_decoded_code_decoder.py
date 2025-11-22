class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        for position, character in enumerate(s):
            index = ord(character) - ord('a')
            current_appeal += position - last[index]
            total_appeal += current_appeal
            last[index] = position
        return total_appeal