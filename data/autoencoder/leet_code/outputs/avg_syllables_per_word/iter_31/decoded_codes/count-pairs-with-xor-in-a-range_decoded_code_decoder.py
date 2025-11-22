from typing import Dict, Optional, List

class TrieNode:
    def __init__(self):
        self.children: Dict[int, 'TrieNode'] = {}
        self.count: int = 0

class Trie:
    def __init__(self, bit_length: int):
        self.root = TrieNode()
        self.bit_length = bit_length

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
        node: Optional[TrieNode] = self.root
        for i in range(self.bit_length, -1, -1):
            if node is None:
                break
            bit = (num >> i) & 1
            threshold_bit = (threshold >> i) & 1
            if threshold_bit == 1:
                count += node.children.get(bit, TrieNode()).count if bit in node.children else 0
                node = node.children.get(bit ^ 1, None)
            else:
                node = node.children.get(bit, None)
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie(15)
        nice_pairs = 0
        for num in nums:
            nice_pairs += trie.count_less_than(num, high + 1) - trie.count_less_than(num, low)
            trie.insert(num)
        return nice_pairs