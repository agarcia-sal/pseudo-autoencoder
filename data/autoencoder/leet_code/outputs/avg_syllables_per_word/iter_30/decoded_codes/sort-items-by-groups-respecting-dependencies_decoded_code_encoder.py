from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign unique group ids to items with no group
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        group_items = defaultdict(list)  # group_id -> list of items
        group_graph = defaultdict(list)  # group_id -> dependent groups
        item_graph = defaultdict(list)   # item_id -> dependent items
        item_in_degree = [0] * n
        group_in_degree = [0] * m

        for i in range(n):
            group_items[group[i]].append(i)

        for i in range(n):
            for before_item in beforeItems[i]:
                if group[before_item] == group[i]:
                    item_graph[before_item].append(i)
                    item_in_degree[i] += 1
                else:
                    group_graph[group[before_item]].append(group[i])
                    group_in_degree[group[i]] += 1

        def topological_sort(graph, in_degree, items):
            queue = deque()
            for item in items:
                if in_degree[item] == 0:
                    queue.append(item)
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
        for items in group_items.values():
            sorted_items = topological_sort(item_graph, item_in_degree[:], items)
            if not sorted_items:
                return []
            sorted_within_groups.extend(sorted_items)

        sorted_groups = topological_sort(group_graph, group_in_degree[:], list(range(m)))
        if not sorted_groups:
            return []

        group_to_items_map = defaultdict(list)
        for item in sorted_within_groups:
            group_to_items_map[group[item]].append(item)

        result = []
        for grp in sorted_groups:
            result.extend(group_to_items_map[grp])

        return result