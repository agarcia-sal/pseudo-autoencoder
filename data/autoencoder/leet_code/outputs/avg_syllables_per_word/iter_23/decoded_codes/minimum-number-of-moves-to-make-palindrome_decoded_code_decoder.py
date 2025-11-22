class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        while len(s) > 1:
            match_found = False
            for i in range(len(s) - 1, 0, -1):
                if s[i] == s[0]:
                    # Move matching element to the end of the list by swapping adjacent elements
                    for j in range(i, len(s) - 1):
                        s[j], s[j + 1] = s[j + 1], s[j]
                        moves += 1
                    # Remove first and last elements, which are now matching pair
                    s.pop(0)
                    s.pop()
                    match_found = True
                    break
            if not match_found:
                # No matching pair for s[0], remove it
                s.pop(0)
        return moves