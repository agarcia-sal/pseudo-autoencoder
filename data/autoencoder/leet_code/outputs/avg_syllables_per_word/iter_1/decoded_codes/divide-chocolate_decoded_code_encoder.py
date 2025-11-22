def maximizeSweetness(sweetness, k):
    def canDivide(min_sweet):
        pieces, curr = 0, 0
        for s in sweetness:
            curr += s
            if curr >= min_sweet:
                pieces += 1
                curr = 0
                if pieces > k:
                    return True
        return pieces > k

    left, right = min(sweetness), sum(sweetness) // (k + 1)
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if canDivide(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res