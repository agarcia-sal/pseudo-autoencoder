from collections import defaultdict
from typing import List, Tuple

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        tree = defaultdict(list)
        for i, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(i)

        node_queries = defaultdict(list)
        for node, value in queries:
            node_queries[node].append(value)

        root = TrieNode()
        result = [0] * len(queries)

        # Map each (node,value) query pair to its index for storing final results
        query_idx = {(node, value): idx for idx, (node, value) in enumerate(queries)}

        def insert(trie_root: TrieNode, value: int) -> None:
            node = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                node = node.children[bit]
                node.count += 1

        def erase(trie_root: TrieNode, value: int) -> None:
            node = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                node = node.children[bit]
                node.count -= 1

        def max_xor(trie_root: TrieNode, value: int) -> int:
            node = trie_root
            max_xor_val = 0
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                toggled_bit = 1 - bit
                if toggled_bit in node.children and node.children[toggled_bit].count > 0:
                    max_xor_val += (1 << i)
                    node = node.children[toggled_bit]
                else:
                    node = node.children[bit]
            return max_xor_val

        def dfs(node: int) -> None:
            insert(root, node)
            for value in node_queries[node]:
                idx = query_idx[(node, value)]
                result[idx] = max_xor(root, value)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        for i, parent in enumerate(parents):
            if parent == -1:
                dfs(i)
                break

        return result