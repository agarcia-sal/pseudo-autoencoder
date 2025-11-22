from typing import Dict, Optional, List


class TrieNode:
    def __init__(self):
        self.children: Dict[int, TrieNode] = {}
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
        node: Optional[TrieNode] = self.root
        for i in range(self.bit_length, -1, -1):
            if node is None:
                break
            bit = (num >> i) & 1
            threshold_bit = (threshold >> i) & 1
            if threshold_bit == 1:
                if bit in node.children:
                    count += node.children[bit].count
                xor_bit = bit ^ 1
                if xor_bit in node.children:
                    node = node.children[xor_bit]
                else:
                    node = None
            else:
                if bit in node.children:
                    node = node.children[bit]
                else:
                    node = None
        return count


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        max_num = max(nums) if nums else 0
        max_val = max(max_num, high)
        bit_length = max_val.bit_length()
        trie = Trie(bit_length)
        nice_pairs = 0
        for num in nums:
            count_high = trie.count_less_than(num, high + 1)
            count_low = trie.count_less_than(num, low)
            nice_pairs += count_high - count_low
            trie.insert(num)
        return nice_pairs