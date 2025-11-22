from typing import List

class Solution:
    def appealSum(self, s: str) -> int:
        last: List[int] = [-1] * 26
        total_appeal = 0
        current_appeal = 0
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            current_appeal += i - last[index]
            total_appeal += current_appeal
            last[index] = i
        return total_appeal