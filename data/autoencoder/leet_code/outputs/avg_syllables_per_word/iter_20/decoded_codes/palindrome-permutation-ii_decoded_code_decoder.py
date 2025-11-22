from collections import Counter
from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        cnt = Counter(s)
        mid = ""
        for c, v in cnt.items():
            if v % 2 == 1:
                if mid:
                    return []
                mid = c
                cnt[c] -= 1

        ans = []
        length = len(s)

        def dfs(t: str) -> None:
            if len(t) == length:
                ans.append(t)
                return
            for c in cnt:
                if cnt[c] >= 2:
                    cnt[c] -= 2
                    dfs(c + t + c)
                    cnt[c] += 2

        dfs(mid)
        return ans