class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def dfs(i: int) -> None:
            if i >= len(t):
                ans.append(''.join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # Toggle case using XOR with 32 on ASCII code
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)
                t[i] = chr(ord(t[i]) ^ 32)  # revert back to original for other calls

        t = list(s)
        ans = []
        dfs(0)
        return ans