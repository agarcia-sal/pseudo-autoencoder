jumps = {
    (1,3):2, (1,7):4, (1,9):5,
    (2,8):5,
    (3,1):2, (3,7):5, (3,9):6,
    (4,6):5,
    (5,5):5,
    (6,4):5,
    (7,1):4, (7,3):5, (7,9):8,
    (8,2):5,
    (9,1):5, (9,3):6, (9,7):8
}

def countPatterns(dot, visited, length, m, n):
    if length == n:
        return 1
    count = 1 if length >= m else 0
    for nxt in range(1, 10):
        if not visited[nxt]:
            j = jumps.get((dot, nxt))
            if not j or visited[j]:
                visited[nxt] = True
                count += countPatterns(nxt, visited, length + 1, m, n)
                visited[nxt] = False
    return count


def totalPatterns(m, n):
    visited = [False] * 10
    res = 0

    visited[1] = True
    res += countPatterns(1, visited, 1, m, n) * 4
    visited[1] = False

    visited[2] = True
    res += countPatterns(2, visited, 1, m, n) * 4
    visited[2] = False

    visited[5] = True
    res += countPatterns(5, visited, 1, m, n)
    visited[5] = False

    return res