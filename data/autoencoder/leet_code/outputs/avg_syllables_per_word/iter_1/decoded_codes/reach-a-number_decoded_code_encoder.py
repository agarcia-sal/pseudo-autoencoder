def steps_to_reach_target(target):
    target = abs(target)
    k, sum_steps = 0, 0
    while sum_steps < target:
        k += 1
        sum_steps += k
    diff = sum_steps - target
    if diff % 2 == 0:
        return k
    else:
        return k + 1 if k % 2 == 0 else k + 2