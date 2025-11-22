def letterCasePermutation(s):
    t = list(s)
    ans = []

    def dfs(i):
        if i == len(t):
            ans.append("".join(t))
            return
        dfs(i + 1)
        if t[i].isalpha():
            t[i] = t[i].swapcase()
            dfs(i + 1)
            t[i] = t[i].swapcase()

    dfs(0)
    return ans