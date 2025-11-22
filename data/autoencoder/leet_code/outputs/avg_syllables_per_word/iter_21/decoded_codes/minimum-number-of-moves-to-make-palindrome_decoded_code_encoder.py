class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0

        while len(s) > 1:
            matching_character_found = False
            for i in range(len(s) - 1, 0, -1):
                if s[i] == s[0]:
                    matching_character_found = True
                    for j in range(i, len(s) - 1):
                        s[j], s[j + 1] = s[j + 1], s[j]  # Swap adjacent characters
                        moves += 1
                    s.pop(0)      # Remove first character
                    s.pop(-1)     # Remove last character
                    break

            if not matching_character_found:
                s.pop(0)

        return moves