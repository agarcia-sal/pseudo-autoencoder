from typing import List, Tuple

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # Each query is (xi, mi) and we also keep original index for result placement
        sorted_queries: List[Tuple[int, int, int]] = sorted(
            [(i, q[0], q[1]) for i, q in enumerate(queries)],
            key=lambda x: x[2]
        )

        result = [-1] * len(queries)
        trie = {}
        num_index = 0

        for query_index, xi, mi in sorted_queries:
            while num_index < len(nums) and nums[num_index] <= mi:
                num = nums[num_index]
                node = trie
                # Insert num into trie bit by bit from 31 down to 0
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                num_index += 1

            if not trie:
                # No numbers inserted for this query, result stays -1
                continue

            node = trie
            max_xor = 0
            # Find max XOR with xi given numbers in trie
            for i in range(31, -1, -1):
                bit = (xi >> i) & 1
                toggle_bit = 1 - bit
                if toggle_bit in node:
                    max_xor |= (1 << i)
                    node = node[toggle_bit]
                else:
                    node = node[bit]

            result[query_index] = max_xor

        return result