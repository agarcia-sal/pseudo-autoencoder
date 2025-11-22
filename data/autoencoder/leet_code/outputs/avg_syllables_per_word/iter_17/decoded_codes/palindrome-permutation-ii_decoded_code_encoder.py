from collections import Counter

class Solution:
    def generatePalindromes(self, s):
        def dfs(t):
            if len(t) == len(s):
                ans.append(t)
                return
            for ch, count in cnt.items():
                if count > 1:
                    cnt[ch] -= 2
                    dfs(ch + t + ch)
                    cnt[ch] += 2

        cnt = Counter(s)
        mid = ''
        for ch, count in cnt.items():
            if count % 2 == 1:
                if mid != '':
                    return []
                mid = ch
                cnt[ch] -= 1
        ans = []
        dfs(mid)
        return ans