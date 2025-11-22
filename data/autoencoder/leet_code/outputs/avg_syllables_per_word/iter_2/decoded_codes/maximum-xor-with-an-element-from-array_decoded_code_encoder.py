from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [-1] * len(queries)
        trie = {}
        num_index = 0

        for query_index, (xi, mi) in sorted_queries:
            while num_index < len(nums) and nums[num_index] <= mi:
                num = nums[num_index]
                node = trie
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                num_index += 1

            if not trie:
                continue

            node = trie
            max_xor = 0
            for i in range(31, -1, -1):
                bit = (xi >> i) & 1
                toggle_bit = 1 - bit
                if toggle_bit in node:
                    max_xor |= (1 << i)
                    node = node[toggle_bit]
                else:
                    node = node.get(bit, {})

            result[query_index] = max_xor

        return result