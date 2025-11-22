from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for index in range(n):
            if group[index] == -1:
                group[index] = m
                m += 1

        group_items = self.initialize_defaultdict_list()
        group_graph = self.initialize_defaultdict_list()
        item_graph = self.initialize_defaultdict_list()
        item_in_degree = [0] * n
        group_in_degree = [0] * m

        for index in range(n):
            group_items[group[index]].append(index)

        for index in range(n):
            for before_element in beforeItems[index]:
                if group[before_element] == group[index]:
                    item_graph[before_element].append(index)
                    item_in_degree[index] += 1
                else:
                    group_graph[group[before_element]].append(group[index])
                    group_in_degree[group[index]] += 1

        def topological_sort(graph, in_degree, items):
            q = deque([item for item in items if in_degree[item] == 0])
            result = []
            while q:
                u = q.popleft()
                result.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q.append(v)
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

        group_to_items_map = self.initialize_defaultdict_list()
        for item in sorted_within_groups:
            group_to_items_map[group[item]].append(item)

        result = []
        for group_element in sorted_groups:
            result.extend(group_to_items_map[group_element])

        return result

    def initialize_defaultdict_list(self):
        return defaultdict(list)