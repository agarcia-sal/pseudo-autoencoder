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
        query_idx = {}
        for i, (node, val) in enumerate(queries):
            node_queries[node].append(val)
            query_idx[(node, val)] = i

        root = TrieNode()
        result = [0] * len(queries)

        def insert(trie_root, value):
            curr = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                curr = curr.children[bit]
                curr.count += 1

        def erase(trie_root, value):
            curr = trie_root
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                curr = curr.children[bit]
                curr.count -= 1

        def max_xor(trie_root, value):
            curr = trie_root
            max_val = 0
            for i in range(17, -1, -1):
                bit = (value >> i) & 1
                toggled = 1 - bit
                if toggled in curr.children and curr.children[toggled].count > 0:
                    max_val |= (1 << i)
                    curr = curr.children[toggled]
                else:
                    curr = curr.children[bit]
            return max_val

        def dfs(node):
            insert(root, node)
            for val in node_queries[node]:
                idx = query_idx[(node, val)]
                result[idx] = max_xor(root, val)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        for i, p in enumerate(parents):
            if p == -1:
                dfs(i)
                break

        return result