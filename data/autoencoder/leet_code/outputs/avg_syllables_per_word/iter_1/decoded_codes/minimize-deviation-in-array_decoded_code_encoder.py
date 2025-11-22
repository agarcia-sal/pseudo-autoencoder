import heapq

def minimum_deviation(nums):
    maxh = []
    min_v = float('inf')

    for n in nums:
        if n % 2 == 1:
            n *= 2
        min_v = min(min_v, n)
        heapq.heappush(maxh, -n)

    min_dev = float('inf')
    while -maxh[0] % 2 == 0:
        x = -heapq.heappop(maxh)
        min_dev = min(min_dev, x - min_v)
        x //= 2
        min_v = min(min_v, x)
        heapq.heappush(maxh, -x)

    min_dev = min(min_dev, -maxh[0] - min_v)
    return min_dev