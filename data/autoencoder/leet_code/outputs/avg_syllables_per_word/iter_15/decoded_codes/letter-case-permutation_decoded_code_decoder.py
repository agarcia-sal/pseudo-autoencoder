from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i: int):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # Flip case using xor 32 (bitwise) between lower and upper case letters
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)
                t[i] = chr(ord(t[i]) ^ 32)  # revert back to original for other branches

        t = list(s)
        ans = []
        dfs(0)
        return ans