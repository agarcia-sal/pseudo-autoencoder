import heapq

def min_difference(nums):
    n = len(nums) // 3
    min_heap = []
    min_sums = [0] * (2 * n + 1)
    curr_sum = 0

    for i in range(2 * n):
        # push negative values to simulate max heap using min heap
        heapq.heappush(min_heap, -nums[i])
        curr_sum += nums[i]
        if len(min_heap) > n:
            removed = -heapq.heappop(min_heap)
            curr_sum -= removed
        if len(min_heap) == n:
            min_sums[i] = curr_sum

    max_heap = []
    max_sums = [0] * (2 * n + 1)
    curr_sum = 0

    for i in range(3 * n - 1, n - 1, -1):
        heapq.heappush(max_heap, nums[i])
        curr_sum += nums[i]
        if len(max_heap) > n:
            removed = heapq.heappop(max_heap)
            curr_sum -= removed
        if len(max_heap) == n:
            max_sums[i] = curr_sum

    min_diff = float('inf')
    for i in range(n - 1, 2 * n):
        min_diff = min(min_diff, min_sums[i] - max_sums[i + 1])

    return min_diff