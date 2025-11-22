from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents, queries):
        tree = defaultdict(list)
        for i, p in enumerate(parents):
            if p != -1:
                tree[p].append(i)

        node_queries = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            node_queries[node].append(val)

        root = TrieNode()
        result = [0] * len(queries)
        query_idx = {(node, val): i for i, (node, val) in enumerate(queries)}

        def insert(trie_root, value):
            node = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                node = node.children[bit]
                node.count += 1

        def erase(trie_root, value):
            node = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                node = node.children[bit]
                node.count -= 1

        def max_xor(trie_root, value):
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

        def dfs(node):
            insert(root, node)
            for val in node_queries[node]:
                result[query_idx[(node, val)]] = max_xor(root, val)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        for i, p in enumerate(parents):
            if p == -1:
                dfs(i)
                break

        return result