from typing import Dict, Optional, List

class TrieNode:
    def __init__(self):
        self.children: Dict[int, "TrieNode"] = {}
        self.count: int = 0

class Trie:
    def __init__(self, bit_length: int):
        self.root: TrieNode = TrieNode()
        self.bit_length: int = bit_length

    def insert(self, num: int) -> None:
        node = self.root
        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def count_less_than(self, num: int, threshold: int) -> int:
        count = 0
        node = self.root
        for i in range(self.bit_length, -1, -1):
            if node is None:
                break
            bit = (num >> i) & 1
            threshold_bit = (threshold >> i) & 1
            if threshold_bit == 1:
                # Add counts of subtree with bit == bit if exists
                count += node.children.get(bit, TrieNode()).count if bit in node.children else 0
                # Move to opposite bit subtree
                node = node.children.get(bit ^ 1, None)
            else:
                # Move to subtree with bit == bit
                node = node.children.get(bit, None)
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        if not nums:
            return 0
        max_num = max(nums)
        max_val = max(max_num, high)
        # Determine bit length from max_val (0-based index)
        bit_length = max_val.bit_length() - 1 if max_val > 0 else 0

        trie = Trie(bit_length)
        nice_pairs = 0
        for num in nums:
            nice_pairs += trie.count_less_than(num, high + 1) - trie.count_less_than(num, low)
            trie.insert(num)
        return nice_pairs