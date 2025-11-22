class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        position_counter = 0
        for character in s:
            index = ord(character) - ord('a')
            difference = position_counter - last[index]
            current_appeal += difference
            total_appeal += current_appeal
            last[index] = position_counter
            position_counter += 1
        return total_appeal