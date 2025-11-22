def min_moves(nums, k):
    pos = [i for i, num in enumerate(nums) if num == 1]

    def calc_cost(s, e):
        mid = (s + e) // 2
        return sum(abs(pos[i] - (pos[mid] - (mid - i))) for i in range(s, e))

    min_c = float('inf')
    for i in range(len(pos) - k + 1):
        min_c = min(min_c, calc_cost(i, i + k))
    return min_c