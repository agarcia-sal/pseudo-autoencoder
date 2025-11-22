class Solution:
    def minMovesToMakePalindrome(self, string_s: str) -> int:
        list_s = list(string_s)
        count_moves = 0

        while len(list_s) > 1:
            match_found = False
            for i in range(len(list_s) - 1, 0, -1):
                if list_s[i] == list_s[0]:
                    # bubble the matched character to the end
                    for j in range(i, len(list_s) - 1):
                        list_s[j], list_s[j + 1] = list_s[j + 1], list_s[j]
                        count_moves += 1
                    # remove matched pair from front and end
                    list_s.pop(0)
                    list_s.pop()
                    match_found = True
                    break
            if not match_found:
                list_s.pop(0)

        return count_moves