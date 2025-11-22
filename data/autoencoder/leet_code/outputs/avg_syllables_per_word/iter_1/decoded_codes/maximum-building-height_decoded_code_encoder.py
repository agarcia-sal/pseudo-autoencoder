restrictions.append([1, 0])
restrictions.sort(key=lambda x: x[0])

for i in range(1, len(restrictions)):
    restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0]))

for i in range(len(restrictions) - 2, -1, -1):
    restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))

max_h = 0
prev_idx, prev_h = restrictions[0]

for i in range(1, len(restrictions)):
    idx, h = restrictions[i]
    max_h = max(max_h, (idx - prev_idx + prev_h + h) // 2)
    prev_idx, prev_h = idx, h

max_h = max(max_h, prev_h + (n - prev_idx))

return max_h