from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        group_items = defaultdict(list)
        group_graph = defaultdict(list)
        item_graph = defaultdict(list)
        item_in_degree = [0] * n
        group_in_degree = [0] * m

        for i in range(n):
            group_items[group[i]].append(i)

        for i in range(n):
            for before_element in beforeItems[i]:
                if group[before_element] == group[i]:
                    item_graph[before_element].append(i)
                    item_in_degree[i] += 1
                else:
                    group_graph[group[before_element]].append(group[i])
                    group_in_degree[group[i]] += 1

        def topological_sort(graph, in_degree, items):
            queue = deque([u for u in items if in_degree[u] == 0])
            result = []
            while queue:
                u = queue.popleft()
                result.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            return result if len(result) == len(items) else []

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
        for grp in sorted_groups:
            result.extend(group_to_items_map[grp])

        return result