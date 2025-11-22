def count_operations(target):
    ops = 0
    prev = 0
    for cur in target:
        if cur > prev:
            ops += cur - prev
        prev = cur
    return ops