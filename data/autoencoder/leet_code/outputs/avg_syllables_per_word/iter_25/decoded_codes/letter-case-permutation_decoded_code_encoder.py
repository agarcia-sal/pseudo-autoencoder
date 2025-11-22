class Solution:
    def letterCasePermutation(self, s):
        def dfs(i):
            if i >= len(t):
                ans.append("".join(t))
                return
            dfs(i + 1)
            if t[i].isalpha():
                # Toggle case using bitwise XOR with 32
                t[i] = chr(ord(t[i]) ^ 32)
                dfs(i + 1)
                t[i] = chr(ord(t[i]) ^ 32)  # revert change after dfs call

        t = list(s)
        ans = []
        dfs(0)
        return ans