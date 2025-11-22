def maximum_requests(n, requests):
    max_requests = 0
    for mask in range(1 << len(requests)):
        balance = [0] * n
        count = 0
        for i in range(len(requests)):
            if mask & (1 << i) != 0:
                f, t = requests[i]
                balance[f] -= 1
                balance[t] += 1
                count += 1
        if all(b == 0 for b in balance):
            max_requests = max(max_requests, count)
    return max_requests