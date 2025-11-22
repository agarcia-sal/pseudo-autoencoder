from typing import List

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0

        while len(s) > 1:
            found_match = False
            for i in range(len(s) - 1, 0, -1):
                if s[i] == s[0]:
                    # Bubble the matching character to the end of the list
                    for j in range(i, len(s) - 1):
                        s[j], s[j + 1] = s[j + 1], s[j]
                        moves += 1
                    # Remove the matched pair from both ends
                    s.pop(0)
                    s.pop()
                    found_match = True
                    break
            if not found_match:
                # No matching character found, remove the first character
                s.pop(0)

        return moves