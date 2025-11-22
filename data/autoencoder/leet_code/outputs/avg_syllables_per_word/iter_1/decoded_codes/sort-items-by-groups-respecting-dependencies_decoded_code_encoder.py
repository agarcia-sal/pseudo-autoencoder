from collections import defaultdict, deque

def sort_items(n, m, group, beforeItems):
    # Assign unique group ids to items with group[i] == -1
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    group_items = defaultdict(list)
    group_graph = defaultdict(list)
    item_graph = defaultdict(list)
    item_in_degree = [0] * n
    group_in_degree = [0] * m

    # Group items by their group id
    for i in range(n):
        group_items[group[i]].append(i)

    # Build graphs and in-degree arrays
    for i in range(n):
        for b in beforeItems[i]:
            if group[b] == group[i]:
                item_graph[b].append(i)
                item_in_degree[i] += 1
            else:
                group_graph[group[b]].append(group[i])
                group_in_degree[group[i]] += 1

    def topo_sort(g, in_deg, elems):
        q = deque([u for u in elems if in_deg[u] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        return res if len(res) == len(elems) else []

    # Topological sort items within each group
    sorted_within = []
    for items in group_items.values():
        # Need to copy in-degree for items in this group for separate topo sort
        in_deg_copy = [item_in_degree[i] for i in range(n)]
        sorted_items = topo_sort(item_graph, in_deg_copy, items)
        if not sorted_items:
            return []
        sorted_within.extend(sorted_items)

    # Topological sort groups
    sorted_groups = topo_sort(group_graph, group_in_degree[:], list(range(m)))
    if not sorted_groups:
        return []

    # Map from group to sorted items
    grp_to_items = defaultdict(list)
    for item in sorted_within:
        grp_to_items[group[item]].append(item)

    # Combine results by group order
    res = []
    for g in sorted_groups:
        res.extend(grp_to_items[g])
    return res