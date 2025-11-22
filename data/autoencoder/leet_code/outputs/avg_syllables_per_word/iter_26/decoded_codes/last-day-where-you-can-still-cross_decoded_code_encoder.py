from typing import List

class UnionFind:
    def __init__(self, number_of_elements: int):
        self.parent = list(range(number_of_elements))
        self.rank = [0] * number_of_elements

    def find(self, element: int) -> int:
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, first_element: int, second_element: int) -> None:
        root_of_first = self.find(first_element)
        root_of_second = self.find(second_element)
        if root_of_first != root_of_second:
            if self.rank[root_of_first] > self.rank[root_of_second]:
                self.parent[root_of_second] = root_of_first
            elif self.rank[root_of_first] < self.rank[root_of_second]:
                self.parent[root_of_first] = root_of_second
            else:
                self.parent[root_of_second] = root_of_first
                self.rank[root_of_first] += 1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[1] * col for _ in range(row)]
        uf = UnionFind(row * col + 2)
        TOP = row * col
        BOTTOM = row * col + 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 0

            index = r * col + c
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    uf.union(index, nr * col + nc)

            if r == 0:
                uf.union(index, TOP)
            if r == row - 1:
                uf.union(index, BOTTOM)

            if uf.find(TOP) == uf.find(BOTTOM):
                return day

        return 0