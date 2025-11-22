from collections import Counter

class Solution:
    def generatePalindromes(self, string_input: str) -> list[str]:
        cnt = Counter(string_input)
        mid = ''
        for ch, val in cnt.items():
            if val & 1:
                if mid != '':
                    return []
                mid = ch
                cnt[ch] -= 1

        ans = []

        def dfs(current_string):
            if len(current_string) == len(string_input):
                ans.append(current_string)
                return
            for ch, val in cnt.items():
                if val > 1:
                    cnt[ch] -= 2
                    dfs(ch + current_string + ch)
                    cnt[ch] += 2

        dfs(mid)
        return ans