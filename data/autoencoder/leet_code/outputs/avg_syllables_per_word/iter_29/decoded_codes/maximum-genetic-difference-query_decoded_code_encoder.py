from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents, queries):
        tree = defaultdict(list)
        for idx, p in enumerate(parents):
            if p != -1:
                tree[p].append(idx)

        node_queries = defaultdict(list)
        for idx, (node_val, val) in enumerate(queries):
            node_queries[node_val].append((val, idx))

        root = TrieNode()
        result = [0] * len(queries)

        def insert(trie_root, value):
            current = trie_root
            for bit_pos in range(17, -1, -1):
                bit = (value >> bit_pos) & 1
                if bit not in current.children:
                    current.children[bit] = TrieNode()
                current = current.children[bit]
                current.count += 1

        def erase(trie_root, value):
            current = trie_root
            for bit_pos in range(17, -1, -1):
                bit = (value >> bit_pos) & 1
                current = current.children[bit]
                current.count -= 1

        def max_xor(trie_root, value):
            current = trie_root
            max_val = 0
            for bit_pos in range(17, -1, -1):
                bit = (value >> bit_pos) & 1
                toggled_bit = 1 - bit
                if toggled_bit in current.children and current.children[toggled_bit].count > 0:
                    max_val |= (1 << bit_pos)
                    current = current.children[toggled_bit]
                else:
                    current = current.children.get(bit, None)
                    # Defensive: current should never be None here if inputs are consistent
                    if current is None:
                        break
            return max_val

        def dfs(node):
            insert(root, node)
            for val, q_idx in node_queries[node]:
                result[q_idx] = max_xor(root, val)
            for child in tree[node]:
                dfs(child)
            erase(root, node)

        for idx, p in enumerate(parents):
            if p == -1:
                dfs(idx)
                break

        return result