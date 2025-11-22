from math import comb

def kthSmallestPath(dest, k):
    row, col = dest
    path = []
    for _ in range(row + col):
        if col > 0:
            paths_H = comb(row + col - 1, col - 1)
            if k <= paths_H:
                path.append('H')
                col -= 1
            else:
                path.append('V')
                row -= 1
                k -= paths_H
        else:
            path.append('V')
            row -= 1
    return ''.join(path)