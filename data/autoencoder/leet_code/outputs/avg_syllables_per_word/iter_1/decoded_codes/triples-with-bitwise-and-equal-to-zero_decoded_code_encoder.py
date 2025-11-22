from collections import defaultdict

freq = defaultdict(int)
for x in nums:
    for y in nums:
        freq[x & y] += 1

res = 0
for z in nums:
    for p, c in freq.items():
        if (p & z) == 0:
            res += c

return res