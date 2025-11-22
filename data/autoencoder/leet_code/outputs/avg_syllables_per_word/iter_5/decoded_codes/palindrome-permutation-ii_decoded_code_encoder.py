from collections import Counter

class Solution:
    def generatePalindromes(self, s):
        cnt = Counter(s)
        mid = ''
        for c, v in cnt.items():
            if v % 2 == 1:
                if mid:
                    return []
                mid = c
                cnt[c] -= 1

        ans = []
        def dfs(t):
            if len(t) == len(s):
                ans.append(t)
                return
            for c in cnt:
                if cnt[c] > 1:
                    cnt[c] -= 2
                    dfs(c + t + c)
                    cnt[c] += 2

        dfs(mid)
        return ans