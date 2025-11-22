class Solution:
    def minMovesToMakePalindrome(self, s):
        s = list(s)
        moves = 0

        while len(s) > 1:
            for i in range(len(s) - 1, 0, -1):
                if s[i] == s[0]:
                    # Move matching character to the end by swapping adjacent characters
                    for j in range(i, len(s) - 1):
                        s[j], s[j + 1] = s[j + 1], s[j]
                        moves += 1
                    # Remove the matched pair
                    s.pop(0)
                    s.pop()
                    break
            else:
                # No matching character found for s[0]
                s.pop(0)

        return moves