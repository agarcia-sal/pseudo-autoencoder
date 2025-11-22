MOD = 10**9 + 7
MAX = max(instructions) + 1
bit = [0] * MAX

def update(i, v):
    while i < MAX:
        bit[i] += v
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

total = 0
for i, num in enumerate(instructions):
    less = query(num - 1)
    greater = i - query(num)
    cost = min(less, greater)
    total = (total + cost) % MOD
    update(num, 1)

return total