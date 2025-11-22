from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        tree = defaultdict(list)
        for idx, p in enumerate(parents):
            if p != -1:
                tree[p].append(idx)

        node_queries = defaultdict(list)
        for i, (node_element, value_element) in enumerate(queries):
            node_queries[node_element].append(value_element)

        query_idx = {(node_element, value_element): i for i, (node_element, value_element) in enumerate(queries)}

        root = TrieNode()
        result = [0] * len(queries)

        def insert(trie_root: TrieNode, value: int) -> None:
            current_node = trie_root
            for bit_index in range(17, -1, -1):
                bit_value = (value >> bit_index) & 1
                current_node = current_node.children[bit_value]
                current_node.count += 1

        def erase(trie_root: TrieNode, value: int) -> None:
            current_node = trie_root
            for bit_index in range(17, -1, -1):
                bit_value = (value >> bit_index) & 1
                current_node = current_node.children[bit_value]
                current_node.count -= 1

        def max_xor(trie_root: TrieNode, value: int) -> int:
            current_node = trie_root
            maximum_xor_value = 0
            for bit_index in range(17, -1, -1):
                bit_value = (value >> bit_index) & 1
                toggled_bit = 1 - bit_value
                if toggled_bit in current_node.children and current_node.children[toggled_bit].count > 0:
                    maximum_xor_value |= (1 << bit_index)
                    current_node = current_node.children[toggled_bit]
                else:
                    current_node = current_node.children[bit_value]
            return maximum_xor_value

        def dfs(node_element: int):
            insert(root, node_element)
            for value_element in node_queries[node_element]:
                idx = query_idx[(node_element, value_element)]
                result[idx] = max_xor(root, value_element)
            for child_element in tree[node_element]:
                dfs(child_element)
            erase(root, node_element)

        for idx, p in enumerate(parents):
            if p == -1:
                dfs(idx)
                break

        return result