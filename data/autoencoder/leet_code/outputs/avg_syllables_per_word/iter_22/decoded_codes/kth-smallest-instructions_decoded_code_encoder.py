from math import comb
from typing import List

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination
        path = []
        total_moves = row + col

        for _ in range(total_moves):
            if col > 0:
                # Number of paths starting with 'H'
                paths_with_H = comb(row + col - 1, col - 1)
                if k <= paths_with_H:
                    path.append('H')
                    col -= 1
                else:
                    path.append('V')
                    row -= 1
                    k -= paths_with_H
            else:
                path.append('V')
                row -= 1

        return ''.join(path)