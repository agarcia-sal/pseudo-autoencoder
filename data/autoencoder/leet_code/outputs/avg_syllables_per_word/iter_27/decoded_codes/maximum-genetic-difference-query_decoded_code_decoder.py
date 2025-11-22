from collections import defaultdict
from typing import List, Dict, Tuple

class TrieNode:
    def __init__(self):
        self.children: Dict[int, TrieNode] = defaultdict(TrieNode)
        self.count: int = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        tree: Dict[int, List[int]] = defaultdict(list)
        for i, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(i)

        node_queries: Dict[int, List[int]] = defaultdict(list)
        for node, val in queries:
            node_queries[node].append(val)

        root = TrieNode()
        result: List[int] = [0] * len(queries)

        query_idx: Dict[Tuple[int, int], int] = {}
        for idx, (node, val) in enumerate(queries):
            query_idx[(node, val)] = idx

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
                child = node.children.get(toggled_bit)
                if child is not None and child.count > 0:
                    max_xor_val |= (1 << i)
                    node = child
                else:
                    node = node.children[bit]
            return max_xor_val

        def dfs(node: int) -> None:
            insert(root, node)
            for val in node_queries[node]:
                idx = query_idx[(node, val)]
                result[idx] = max_xor(root, val)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        # Find the root node (parent == -1) and start DFS
        for i, parent in enumerate(parents):
            if parent == -1:
                dfs(i)
                break

        return result