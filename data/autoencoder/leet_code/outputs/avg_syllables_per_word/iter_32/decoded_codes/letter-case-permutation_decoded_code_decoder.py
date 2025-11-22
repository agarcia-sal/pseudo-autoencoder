from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i: int):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # Toggle the case of t[i]
                t[i] = t[i].swapcase()
                dfs(i + 1)
                # Revert back for other DFS paths
                t[i] = t[i].swapcase()

        t = list(s)
        ans = []
        dfs(0)
        return ans