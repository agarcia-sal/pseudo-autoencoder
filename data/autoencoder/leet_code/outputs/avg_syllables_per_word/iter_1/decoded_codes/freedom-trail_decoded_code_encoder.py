from collections import defaultdict
from functools import lru_cache

def find_rotate_steps(ring: str, key: str) -> int:
    n = len(ring)
    positions = defaultdict(list)
    for i, ch in enumerate(ring):
        positions[ch].append(i)

    @lru_cache(None)
    def dp(i, pos):
        if i == len(key):
            return 0
        res = float('inf')
        for p in positions[key[i]]:
            step = min((p - pos) % n, (pos - p) % n)
            res = min(res, step + 1 + dp(i + 1, p))
        return res

    return dp(0, 0)