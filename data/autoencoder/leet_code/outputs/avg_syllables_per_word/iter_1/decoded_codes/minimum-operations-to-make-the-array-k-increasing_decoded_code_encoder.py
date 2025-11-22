from bisect import bisect_right

def kIncreasing(arr, k):
    def LIS(seq):
        lis = []
        for x in seq:
            if not lis or x >= lis[-1]:
                lis.append(x)
            else:
                idx = bisect_right(lis, x)
                lis[idx] = x
        return len(lis)

    ops = 0
    for start in range(k):
        sub = [arr[i] for i in range(start, len(arr), k)]
        ops += len(sub) - LIS(sub)
    return ops