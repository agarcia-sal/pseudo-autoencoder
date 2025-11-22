def getCollisionTimes(cars):
    inf = float('inf')
    n = len(cars)
    result = [-1.0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        pos, spd = cars[i]

        while stack:
            j = stack[-1]
            next_pos, next_spd = cars[j]

            if spd <= next_spd:
                stack.pop()
                continue

            t = (next_pos - pos) / (spd - next_spd)

            if result[j] > 0 and t >= result[j]:
                stack.pop()
                continue

            result[i] = t
            break

        stack.append(i)

    return result