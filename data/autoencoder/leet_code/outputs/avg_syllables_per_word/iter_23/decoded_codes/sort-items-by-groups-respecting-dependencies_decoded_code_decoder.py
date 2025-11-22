from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign unique group IDs to items with no group (-1)
        for index in range(n):
            if group[index] == -1:
                group[index] = m
                m += 1

        group_items = defaultdict(list)  # group_id -> list of items
        group_graph = defaultdict(list)  # group_id -> list of group_ids
        item_graph = defaultdict(list)   # item -> list of items
        item_in_degree = [0] * n
        group_in_degree = [0] * m

        # Populate group_items
        for index in range(n):
            group_items[group[index]].append(index)

        # Build graphs and in-degree arrays
        for index in range(n):
            current_group = group[index]
            for before_element in beforeItems[index]:
                before_group = group[before_element]
                if before_group == current_group:
                    item_graph[before_element].append(index)
                    item_in_degree[index] += 1
                else:
                    group_graph[before_group].append(current_group)
                    group_in_degree[current_group] += 1

        def topological_sort(graph: dict, in_degree: List[int], items: List[int]) -> List[int]:
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
        for items in group_items.values():
            # Note: item_in_degree and item_graph are shared for all groups,
            # but since we only consider subset items, we should copy in_degree
            # and graph for the subgraph induced by items before topological sort.
            # The pseudocode uses the global item_graph and item_in_degree directly,
            # but this might give incorrect results if cycles are outside this group.
            # To faithfully replicate pseudocode, we run topological_sort directly on them.

            # To handle this properly, we create a subgraph and in-degree for the current group items:
            sub_in_degree = {}
            sub_graph = defaultdict(list)
            items_set = set(items)
            for item in items:
                sub_in_degree[item] = item_in_degree[item]
            for u in items:
                for v in item_graph[u]:
                    if v in items_set:
                        sub_graph[u].append(v)

            # Filter sub_in_degree by items only
            # Run topological sort on subgraph
            sorted_items = topological_sort(sub_graph, sub_in_degree, items)
            if not sorted_items:
                return []
            sorted_within_groups.extend(sorted_items)

        # Topological sort of groups
        all_groups = list(range(m))
        sorted_groups = topological_sort(group_graph, group_in_degree, all_groups)
        if not sorted_groups:
            return []

        group_to_items_map = defaultdict(list)
        for item in sorted_within_groups:
            group_to_items_map[group[item]].append(item)

        result = []
        for g in sorted_groups:
            result.extend(group_to_items_map.get(g, []))

        return result