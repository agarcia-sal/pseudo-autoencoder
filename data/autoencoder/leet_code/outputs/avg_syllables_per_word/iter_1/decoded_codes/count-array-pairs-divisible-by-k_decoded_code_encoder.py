from collections import Counter
from math import gcd

def countPairs(nums, k):
    cnt = Counter(gcd(num, k) for num in nums)
    gcds = list(cnt.keys())
    res = 0
    for i in range(len(gcds)):
        for j in range(i, len(gcds)):
            g1, g2 = gcds[i], gcds[j]
            if (g1 * g2) % k == 0:
                if i == j:
                    res += cnt[g1] * (cnt[g1] - 1) // 2
                else:
                    res += cnt[g1] * cnt[g2]
    return res