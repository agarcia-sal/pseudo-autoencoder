from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        tree = defaultdict(list)
        for index, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(index)

        node_queries = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            node_queries[node].append(val)

        root = TrieNode()
        result = [0] * len(queries)

        query_idx = {}
        for i, (node, val) in enumerate(queries):
            query_idx[(node, val)] = i

        def insert(trie_root: TrieNode, value: int) -> None:
            node = trie_root
            for bit_index in range(17, -1, -1):
                bit = (value >> bit_index) & 1
                node = node.children[bit]
                node.count += 1

        def erase(trie_root: TrieNode, value: int) -> None:
            node = trie_root
            for bit_index in range(17, -1, -1):
                bit = (value >> bit_index) & 1
                node = node.children[bit]
                node.count -= 1

        def max_xor(trie_root: TrieNode, value: int) -> int:
            node = trie_root
            max_xor_val = 0
            for bit_index in range(17, -1, -1):
                bit = (value >> bit_index) & 1
                toggled_bit = 1 - bit
                if toggled_bit in node.children and node.children[toggled_bit].count > 0:
                    max_xor_val |= (1 << bit_index)
                    node = node.children[toggled_bit]
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

        for i, parent in enumerate(parents):
            if parent == -1:
                dfs(i)
                break

        return result