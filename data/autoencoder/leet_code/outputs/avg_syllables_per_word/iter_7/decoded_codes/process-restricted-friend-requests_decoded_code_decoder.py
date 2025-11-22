from typing import List, Dict, Set

class UnionFind:
    def __init__(self, n: int):
        self.parent: List[int] = list(range(n))
        self.size: List[int] = [1] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
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
    def friendRequests(
        self,
        n: int,
        restrictions: List[List[int]],
        requests: List[List[int]]
    ) -> List[bool]:

        uf = UnionFind(n)
        result: List[bool] = []
        restriction_map: Dict[int, Set[int]] = {}

        for x, y in restrictions:
            if x not in restriction_map:
                restriction_map[x] = set()
            if y not in restriction_map:
                restriction_map[y] = set()
            restriction_map[x].add(y)
            restriction_map[y].add(x)

        def can_union(u: int, v: int) -> bool:
            root_u = uf.find(u)
            root_v = uf.find(v)

            for person in restriction_map.get(root_u, set()):
                if uf.find(person) == root_v:
                    return False

            for person in restriction_map.get(root_v, set()):
                if uf.find(person) == root_u:
                    return False

            return True

        for u, v in requests:
            if uf.find(u) == uf.find(v):
                result.append(True)
            elif can_union(u, v):
                uf.union(u, v)
                result.append(True)
            else:
                result.append(False)

        return result