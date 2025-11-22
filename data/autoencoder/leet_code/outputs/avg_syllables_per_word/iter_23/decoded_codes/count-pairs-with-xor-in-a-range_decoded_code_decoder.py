from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self, bit_length: int = 15):
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
        node = self.root
        for i in range(self.bit_length, -1, -1):
            if node is None:
                break
            bit = (num >> i) & 1
            threshold_bit = (threshold >> i) & 1
            if threshold_bit == 1:
                if bit in node.children:
                    count += node.children[bit].count
                node = node.children.get(bit ^ 1, None)
            else:
                node = node.children.get(bit, None)
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        nice_pairs = 0
        for num in nums:
            nice_pairs += trie.count_less_than(num, high + 1) - trie.count_less_than(num, low)
            trie.insert(num)
        return nice_pairs