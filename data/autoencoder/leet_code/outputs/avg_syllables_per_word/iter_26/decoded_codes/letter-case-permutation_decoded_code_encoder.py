class Solution:
    def letterCasePermutation(self, s):
        def dfs(i):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                t[i] = t[i].swapcase()  # Toggle case
                dfs(i + 1)
                t[i] = t[i].swapcase()  # Revert to original after recursion

        t = list(s)
        ans = []
        dfs(0)
        return ans