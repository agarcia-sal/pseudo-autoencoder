class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        for index, char in enumerate(s):
            index_value = ord(char) - ord('a')
            current_appeal += index - last[index_value]
            total_appeal += current_appeal
            last[index_value] = index
        return total_appeal