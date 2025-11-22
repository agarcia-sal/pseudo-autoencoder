class UnionFind:
    def __init__(self, number_of_elements):
        self.parent = list(range(number_of_elements))
        self.rank = [1] * number_of_elements

    def find(self, element_u):
        if self.parent[element_u] != element_u:
            self.parent[element_u] = self.find(self.parent[element_u])
        return self.parent[element_u]

    def union(self, element_u, element_v):
        rootU = self.find(element_u)
        rootV = self.find(element_v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, number_of_vertices, list_of_edges):
        for index_position, current_edge in enumerate(list_of_edges):
            current_edge.append(index_position)

        list_of_edges.sort(key=lambda x: x[2])

        def mst(exclude_edge=None, include_edge=None):
            uf = UnionFind(number_of_vertices)
            total_weight = 0

            if include_edge is not None:
                uf.union(include_edge[0], include_edge[1])
                total_weight += include_edge[2]

            for edge_u, edge_v, edge_weight, edge_index in list_of_edges:
                if edge_index == exclude_edge:
                    continue
                if uf.union(edge_u, edge_v):
                    total_weight += edge_weight

            root_of_zero = uf.find(0)
            for i in range(number_of_vertices):
                if uf.find(i) != root_of_zero:
                    return float('inf')

            return total_weight

        minimum_spanning_tree_weight = mst()

        list_of_critical_edges = []
        list_of_pseudo_critical_edges = []

        for edge_u, edge_v, edge_weight, edge_index in list_of_edges:
            if mst(exclude_edge=edge_index) > minimum_spanning_tree_weight:
                list_of_critical_edges.append(edge_index)
            elif mst(include_edge=(edge_u, edge_v, edge_weight)) == minimum_spanning_tree_weight:
                list_of_pseudo_critical_edges.append(edge_index)

        return [list_of_critical_edges, list_of_pseudo_critical_edges]