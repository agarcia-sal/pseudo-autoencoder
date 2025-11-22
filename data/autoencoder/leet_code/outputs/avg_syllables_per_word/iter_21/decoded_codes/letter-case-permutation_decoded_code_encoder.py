class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def dfs(i: int) -> None:
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # Flip case using bitwise XOR with 32 (diff between uppercase and lowercase in ASCII)
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)
                t[i] = chr(ord(t[i]) ^ 32)  # revert to original to backtrack

        t = list(s)
        ans = []
        dfs(0)
        return ans