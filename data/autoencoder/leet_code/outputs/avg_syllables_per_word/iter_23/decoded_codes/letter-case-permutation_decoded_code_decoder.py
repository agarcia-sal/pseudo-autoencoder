class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        def dfs(i: int) -> None:
            if i >= len(t):
                ans.append(''.join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                t[i] = t[i].swapcase()
                dfs(i + 1)
                t[i] = t[i].swapcase()  # revert the change for backtracking

        t = list(s)
        ans = []
        dfs(0)
        return ans