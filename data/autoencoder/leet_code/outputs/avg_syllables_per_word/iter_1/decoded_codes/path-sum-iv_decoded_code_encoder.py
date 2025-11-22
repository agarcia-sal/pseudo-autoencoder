def pathSum(nums):
    tree = {}
    for num in nums:
        d, p, v = num // 100, (num // 10) % 10, num % 10
        tree[(d, p)] = v

    def dfs(d, p, s):
        val = tree.get((d, p))
        if val is None:
            return 0
        s += val
        l, r = (d + 1, 2 * p - 1), (d + 1, 2 * p)
        if l not in tree and r not in tree:
            return s
        return dfs(l[0], l[1], s) + dfs(r[0], r[1], s)

    return dfs(1, 1, 0)