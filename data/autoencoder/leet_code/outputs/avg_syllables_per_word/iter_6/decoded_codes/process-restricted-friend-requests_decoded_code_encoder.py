class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] > self.size[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            else:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]


class Solution:
    def friendRequests(self, n, restrictions, requests):
        uf = UnionFind(n)
        result = []
        restriction_map = {}

        for x, y in restrictions:
            restriction_map.setdefault(x, set()).add(y)
            restriction_map.setdefault(y, set()).add(x)

        def can_union(u, v):
            root_u = uf.find(u)
            root_v = uf.find(v)

            for person in restriction_map.get(root_u, ()):
                if uf.find(person) == root_v:
                    return False
            for person in restriction_map.get(root_v, ()):
                if uf.find(person) == root_u:
                    return False
            return True

        for u, v in requests:
            root_u = uf.find(u)
            root_v = uf.find(v)
            if root_u == root_v:
                result.append(True)
            elif can_union(u, v):
                uf.union(u, v)
                # After union, update restriction_map root keys to merged root
                new_root = uf.find(u)
                old_root = root_v if new_root == root_u else root_u
                # Merge restricted sets
                new_set = restriction_map.get(new_root, set())
                old_set = restriction_map.get(old_root, set())
                merged_set = new_set.union(old_set)
                # Remove old_root key
                if old_root in restriction_map:
                    del restriction_map[old_root]
                # Update restriction sets to refer to new_root
                restriction_map[new_root] = merged_set
                # Update other sets: replace old_root with new_root
                for key in merged_set:
                    if key in restriction_map:
                        if old_root in restriction_map[key]:
                            restriction_map[key].remove(old_root)
                        restriction_map[key].add(new_root)

                result.append(True)
            else:
                result.append(False)

        return result