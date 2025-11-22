class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [-1] * len(queries)
        trie = {}
        num_index = 0

        for qi, (x, m) in indexed_queries:
            while num_index < len(nums) and nums[num_index] <= m:
                node = trie
                num = nums[num_index]
                for i in reversed(range(32)):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                num_index += 1

            if not trie:
                continue

            node = trie
            max_xor = 0
            for i in reversed(range(32)):
                bit = (x >> i) & 1
                toggled = 1 - bit
                if toggled in node:
                    max_xor |= (1 << i)
                    node = node[toggled]
                else:
                    node = node.get(bit, {})

            result[qi] = max_xor

        return result