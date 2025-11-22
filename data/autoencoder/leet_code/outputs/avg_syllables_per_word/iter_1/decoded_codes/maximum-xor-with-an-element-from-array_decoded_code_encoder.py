def maximize_xor(nums, queries):
    nums.sort()
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
    res = [-1] * len(queries)
    trie = {}
    i = 0
    for q_idx, (x, m) in sorted_queries:
        while i < len(nums) and nums[i] <= m:
            n, node = nums[i], trie
            for b in range(31, -1, -1):
                bit = (n >> b) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
            i += 1
        if not trie:
            continue
        node, val = trie, 0
        for b in range(31, -1, -1):
            bit = (x >> b) & 1
            t_bit = 1 - bit
            if t_bit in node:
                val |= (1 << b)
                node = node[t_bit]
            else:
                node = node[bit]
        res[q_idx] = val
    return res