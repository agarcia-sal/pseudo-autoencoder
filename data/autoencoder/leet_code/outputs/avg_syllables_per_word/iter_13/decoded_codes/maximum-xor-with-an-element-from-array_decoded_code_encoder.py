from typing import List, Dict

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # Pair each query with its original index and sort by the mi value (second element)
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])

        result = [-1] * len(queries)
        trie: Dict[int, Dict] = {}
        num_index = 0

        for query_index, (xi, mi) in sorted_queries:
            # Insert nums <= mi into the trie
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
                # No nums inserted <= mi, result stays -1
                continue

            node = trie
            max_xor = 0
            for i in range(31, -1, -1):
                bit = (xi >> i) & 1
                toggle_bit = 1 - bit
                if toggle_bit in node:
                    max_xor |= 1 << i
                    node = node[toggle_bit]
                else:
                    node = node[bit]
            result[query_index] = max_xor

        return result