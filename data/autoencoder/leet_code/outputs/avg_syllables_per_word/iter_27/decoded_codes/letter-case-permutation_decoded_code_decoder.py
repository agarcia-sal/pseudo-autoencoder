from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i: int):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                t[i] = t[i].swapcase()
                dfs(i + 1)
                t[i] = t[i].swapcase()  # revert change

        t = list(s)
        ans: List[str] = []
        dfs(0)
        return ans