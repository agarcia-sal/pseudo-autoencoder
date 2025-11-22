def constructArray(n, k):
    res = list(range(1, n - k))
    left, right = n - k, n
    while left <= right:
        if left == right:
            res.append(left)
        else:
            res.append(left)
            res.append(right)
        left += 1
        right -= 1
    return res