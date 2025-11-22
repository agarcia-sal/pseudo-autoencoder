from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
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
            for before in beforeItems[i]:
                if group[before] == group[i]:
                    item_graph[before].append(i)
                    item_in_degree[i] += 1
                else:
                    group_graph[group[before]].append(group[i])
                    group_in_degree[group[i]] += 1

        def topological_sort(graph: dict[int, list[int]], in_degree: list[int], items: list[int]) -> list[int]:
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
        for items_in_group in group_items.values():
            sorted_items = topological_sort(item_graph, item_in_degree, items_in_group)
            if not sorted_items:
                return []
            sorted_within_groups.extend(sorted_items)

        sorted_groups = topological_sort(group_graph, group_in_degree, list(range(m)))
        if not sorted_groups:
            return []

        group_to_items_map = defaultdict(list)
        for item in sorted_within_groups:
            group_to_items_map[group[item]].append(item)

        result = []
        for group_element in sorted_groups:
            result.extend(group_to_items_map[group_element])

        return result