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
            node_queries[node].append((val, idx))

        root = TrieNode()
        result = [0] * len(queries)

        def insert(trie_root, value):
            cur = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                cur = cur.children[bit]
                cur.count += 1

        def erase(trie_root, value):
            cur = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                cur = cur.children[bit]
                cur.count -= 1

        def max_xor(trie_root, value):
            cur = trie_root
            max_val = 0
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                toggled_bit = 1 - bit
                if toggled_bit in cur.children and cur.children[toggled_bit].count > 0:
                    max_val |= (1 << i)
                    cur = cur.children[toggled_bit]
                else:
                    cur = cur.children[bit]
            return max_val

        def dfs(node):
            insert(root, node)
            for val, idx in node_queries[node]:
                result[idx] = max_xor(root, val)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        root_node = None
        for i, p in enumerate(parents):
            if p == -1:
                root_node = i
                break

        dfs(root_node)
        return result