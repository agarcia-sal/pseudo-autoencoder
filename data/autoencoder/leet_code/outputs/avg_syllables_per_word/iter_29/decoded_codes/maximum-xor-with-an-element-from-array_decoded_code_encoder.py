from typing import List, Dict

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # Pair each query with its original index, then sort by m (max allowed value)
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [-1] * len(queries)
        trie: Dict[int, Dict] = {}
        num_index = 0
        n = len(nums)

        for query_index, (xi, mi) in sorted_queries:
            # Insert nums into trie as long as nums[num_index] <= mi
            while num_index < n and nums[num_index] <= mi:
                num = nums[num_index]
                node = trie
                for i in reversed(range(32)):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                num_index += 1

            if not trie:
                # No numbers inserted for this query, result remains -1
                continue

            node = trie
            max_xor = 0
            for i in reversed(range(32)):
                bit = (xi >> i) & 1
                toggle_bit = 1 - bit
                if toggle_bit in node:
                    max_xor |= (1 << i)
                    node = node[toggle_bit]
                else:
                    node = node.get(bit, None)
                    # Since the trie is constructed from nums that are <= mi, node must exist
                    # but we safeguard in case of malformed trie
                    if node is None:
                        break

            result[query_index] = max_xor

        return result