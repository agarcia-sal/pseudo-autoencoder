from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for index in range(n):
            if group[index] == -1:
                group[index] = m
                m += 1

        group_items = defaultdict(list)
        group_graph = defaultdict(list)
        item_graph = defaultdict(list)

        item_in_degree = [0] * n
        group_in_degree = [0] * m

        for index in range(n):
            group_items[group[index]].append(index)

        for index in range(n):
            for before in beforeItems[index]:
                if group[before] == group[index]:
                    # Same group, item dependency
                    item_graph[before].append(index)
                    item_in_degree[index] += 1
                else:
                    # Different groups, group dependency
                    group_graph[group[before]].append(group[index])
                    group_in_degree[group[index]] += 1

        def topological_sort(graph: defaultdict(list), in_degree: List[int], items: List[int]) -> List[int]:
            queue = deque([item for item in items if in_degree[item] == 0])
            result = []
            while queue:
                u = queue.popleft()
                result.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            if len(result) == len(items):
                return result
            else:
                return []

        sorted_within_groups = []
        for items_list in group_items.values():
            sorted_items = topological_sort(item_graph, item_in_degree.copy(), items_list)
            if not sorted_items:
                return []
            sorted_within_groups.extend(sorted_items)

        sorted_groups = topological_sort(group_graph, group_in_degree.copy(), list(range(m)))
        if not sorted_groups:
            return []

        group_to_items_map = defaultdict(list)
        for item in sorted_within_groups:
            group_to_items_map[group[item]].append(item)

        result = []
        for group_element in sorted_groups:
            result.extend(group_to_items_map[group_element])

        return result