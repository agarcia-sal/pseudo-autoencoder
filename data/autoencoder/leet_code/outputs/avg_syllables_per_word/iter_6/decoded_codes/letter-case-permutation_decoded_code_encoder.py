class Solution:
    def letterCasePermutation(self, s):
        def dfs(i):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)
                t[i] = chr(ord(t[i]) ^ 32)

        t = list(s)
        ans = []
        dfs(0)
        return ans