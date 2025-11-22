from collections import defaultdict
from math import gcd

class Solution:
    def getCoprimes(self, nums, edges):
        number_of_nodes = len(nums)
        tree_structure = self.build_tree(number_of_nodes, edges)
        coprime_matrix = self.precompute_coprime_pairs()

        result_array = self.initialize_result_array(number_of_nodes)
        ancestor_stack = self.initialize_ancestor_stack()

        def dfs(node, parent, depth):
            closest_ancestor = -1
            maximum_depth = -1
            node_value = nums[node]
            for value in range(1, 51):
                if coprime_matrix[node_value][value] and ancestor_stack[value] is not None:
                    ancestor_node, ancestor_depth = ancestor_stack[value]
                    if ancestor_depth > maximum_depth:
                        maximum_depth = ancestor_depth
                        closest_ancestor = ancestor_node
            result_array[node] = closest_ancestor

            original_ancestor = ancestor_stack[node_value]
            ancestor_stack[node_value] = (node, depth)

            for child in tree_structure[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[node_value] = original_ancestor

        dfs(0, -1, 0)
        return result_array

    def build_tree(self, number_of_nodes, edges):
        tree_structure = defaultdict(list)
        for u, v in edges:
            tree_structure[u].append(v)
            tree_structure[v].append(u)
        return tree_structure

    def precompute_coprime_pairs(self):
        size = 51
        coprime_matrix = [[False] * size for _ in range(size)]
        for i in range(1, size):
            for j in range(1, size):
                if gcd(i, j) == 1:
                    coprime_matrix[i][j] = True
        return coprime_matrix

    def initialize_result_array(self, size):
        return [-1] * size

    def initialize_ancestor_stack(self):
        return [None] * 51