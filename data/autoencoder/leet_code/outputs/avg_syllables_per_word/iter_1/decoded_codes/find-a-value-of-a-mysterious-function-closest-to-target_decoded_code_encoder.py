def closestToTarget(arr, target):
    seen, ans = set(), float('inf')
    for num in arr:
        seen = {num & x for x in seen} | {num}
        for val in seen:
            ans = min(ans, abs(val - target))
    return ans