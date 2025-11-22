def find_min_moves(machines):
    sum_d = sum(machines)
    n = len(machines)
    if sum_d % n != 0:
        return -1
    target = sum_d // n
    left_sum = 0
    max_moves = 0
    for i in range(n):
        left_excess = left_sum - target * i
        right_excess = (sum_d - left_sum - machines[i]) - target * (n - i - 1)
        cur = max(abs(left_excess), abs(right_excess), machines[i] - target)
        max_moves = max(max_moves, cur)
        left_sum += machines[i]
    return max_moves