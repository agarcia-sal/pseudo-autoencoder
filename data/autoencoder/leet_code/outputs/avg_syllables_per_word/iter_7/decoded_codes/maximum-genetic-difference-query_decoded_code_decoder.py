from collections import defaultdict
from typing import List, Tuple, Dict

class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[int, TrieNode] = defaultdict(TrieNode)
        self.count: int = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        tree: Dict[int, List[int]] = defaultdict(list)
        for i, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(i)

        node_queries: Dict[int, List[int]] = defaultdict(list)
        for node, val in queries:
            node_queries[node].append(val)

        root = TrieNode()
        result = [0] * len(queries)

        query_idx: Dict[Tuple[int, int], int] = {}
        for i, (node, val) in enumerate(queries):
            query_idx[(node, val)] = i

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
                    max_xor_val |= (1 << i)
                    node = node.children[toggled_bit]
                else:
                    node = node.children[bit]
            return max_xor_val

        def dfs(node_id: int) -> None:
            insert(root, node_id)
            for val in node_queries[node_id]:
                idx = query_idx[(node_id, val)]
                result[idx] = max_xor(root, val)
            for child in tree[node_id]:
                dfs(child)
            erase(root, node_id)

        for i, parent in enumerate(parents):
            if parent == -1:
                dfs(i)
                break

        return result