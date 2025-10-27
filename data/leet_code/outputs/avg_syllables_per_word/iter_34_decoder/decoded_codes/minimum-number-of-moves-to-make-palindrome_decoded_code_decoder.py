class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        while len(s) > 1:
            found_match = False
            for i in range(len(s) - 1, 0, -1):
                if s[i] == s[0]:
                    for j in range(i, len(s) - 1):
                        s[j], s[j + 1] = s[j + 1], s[j]
                        moves += 1
                    s.pop(0)
                    s.pop()
                    found_match = True
                    break
            if not found_match:
                s.pop(0)
        return moves