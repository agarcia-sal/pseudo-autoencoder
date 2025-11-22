def request_will_be_sent(x, y):
    return not (y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100))

def total_requests(ages):
    count = [0] * 121
    for age in ages:
        count[age] += 1

    total = 0
    for x in range(1, 121):
        for y in range(1, 121):
            if request_will_be_sent(x, y):
                total += count[x] * (count[y] - (1 if x == y else 0))

    return total