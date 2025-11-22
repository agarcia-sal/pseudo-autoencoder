from typing import List

class Solution:
    def appealSum(self, s: str) -> int:
        # last[i] stores the last index where character chr(i + ord('a')) appeared.
        last: List[int] = [-1] * 26
        total_appeal = 0
        current_appeal = 0

        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            # Update current appeal by adding new substrings contributed by s[i]
            current_appeal += i - last[index]
            total_appeal += current_appeal
            last[index] = i

        return total_appeal