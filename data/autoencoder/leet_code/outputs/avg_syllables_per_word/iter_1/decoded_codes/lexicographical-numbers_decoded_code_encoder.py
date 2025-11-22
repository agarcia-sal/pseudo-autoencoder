def lexicalOrder(n):
    result = []
    def dfs(x):
        if x > n:
            return
        result.append(x)
        for i in range(10):
            if x * 10 + i > n:
                return
            dfs(x * 10 + i)
    for i in range(1, 10):
        dfs(i)
    return result