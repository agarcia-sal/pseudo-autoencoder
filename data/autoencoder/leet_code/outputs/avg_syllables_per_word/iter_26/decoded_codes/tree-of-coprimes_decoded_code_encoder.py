from math import gcd
from collections import defaultdict
from typing import List, Tuple, Optional

class Solution:
    def getCoprimes(self, numbers_list: List[int], edges_list: List[List[int]]) -> List[int]:
        number_of_nodes = len(numbers_list)

        adjacency_tree = defaultdict(list)
        for current_node, connected_node in edges_list:
            adjacency_tree[current_node].append(connected_node)
            adjacency_tree[connected_node].append(current_node)

        # Precompute coprime relationships for numbers 1 to 50 (inclusive)
        coprime_matrix = [[False] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime_matrix[i][j] = (gcd(i, j) == 1)

        result_array = [-1] * number_of_nodes
        # ancestor_stack will store tuples of (node, depth) or None,
        # indexed by value in numbers_list (which ranges 1 to 50)
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None] * 51

        def dfs(current_node: int, parent_node: int, current_depth: int) -> None:
            closest_coprime_ancestor = -1
            maximum_ancestor_depth = -1
            current_value = numbers_list[current_node]

            # Find closest ancestor with value coprime to current_value
            for value_index in range(1, 51):
                if coprime_matrix[current_value][value_index]:
                    ancestor_info = ancestor_stack[value_index]
                    if ancestor_info is not None:
                        ancestor_node, ancestor_depth = ancestor_info
                        if ancestor_depth > maximum_ancestor_depth:
                            maximum_ancestor_depth = ancestor_depth
                            closest_coprime_ancestor = ancestor_node

            result_array[current_node] = closest_coprime_ancestor

            # Save original ancestor for rollback after DFS
            original_ancestor = ancestor_stack[current_value]
            ancestor_stack[current_value] = (current_node, current_depth)

            for child_node in adjacency_tree[current_node]:
                if child_node != parent_node:
                    dfs(child_node, current_node, current_depth + 1)

            # Restore original ancestor after visiting descendants
            ancestor_stack[current_value] = original_ancestor

        dfs(0, -1, 0)
        return result_array