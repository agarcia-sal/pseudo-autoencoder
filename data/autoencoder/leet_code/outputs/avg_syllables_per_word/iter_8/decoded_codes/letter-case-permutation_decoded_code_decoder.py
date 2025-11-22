class Solution:
    def letterCasePermutation(self, s):
        def dfs(i):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # toggle case
                t[i] = t[i].swapcase()
                dfs(i + 1)
                # revert back for other calls
                t[i] = t[i].swapcase()

        t = list(s)
        ans = []
        dfs(0)
        return ans