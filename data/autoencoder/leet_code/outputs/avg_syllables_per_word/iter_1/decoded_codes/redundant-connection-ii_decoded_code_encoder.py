def find(parent, i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] > rank[ry]:
        parent[ry] = rx
    elif rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        rank[rx] += 1
    return True

def find_redundant_connection(n, edges):
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    candidate1 = candidate2 = last = None

    for u, v in edges:
        if parent[v] != v:
            candidate1 = [parent[v], v]
            candidate2 = [u, v]
        elif not union(parent, rank, u, v):
            last = [u, v]

    if candidate1 is None:
        return last
    if last:
        return candidate1
    return candidate2