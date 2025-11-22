from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # Pair each query with its index and sort by the second element (mi)
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [-1] * len(queries)
        trie = {}
        num_index = 0
        n = len(nums)

        for query_index, (xi, mi) in sorted_queries:
            # Insert nums[num_index] <= mi into trie
            while num_index < n and nums[num_index] <= mi:
                num = nums[num_index]
                node = trie
                for bit_position in range(31, -1, -1):
                    bit_value = (num >> bit_position) & 1
                    if bit_value not in node:
                        node[bit_value] = {}
                    node = node[bit_value]
                num_index += 1

            if not trie:
                continue

            node = trie
            max_xor = 0
            for bit_position in range(31, -1, -1):
                bit_value = (xi >> bit_position) & 1
                toggle_bit = 1 - bit_value
                if toggle_bit in node:
                    max_xor |= (1 << bit_position)
                    node = node[toggle_bit]
                else:
                    node = node.get(bit_value)
                    if node is None:
                        break
            result[query_index] = max_xor

        return result