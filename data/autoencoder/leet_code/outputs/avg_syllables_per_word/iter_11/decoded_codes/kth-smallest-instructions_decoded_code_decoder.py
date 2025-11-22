from math import comb

class Solution:
    def kthSmallestPath(self, destination, k):
        row = destination[0]
        col = destination[1]
        path = []
        total_moves = col + row
        for _ in range(total_moves):
            if col > 0:
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