def min_trips(boxes, maxBoxes, maxWeight):
    n = len(boxes)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    left = 0
    weight = 0
    trips = 0

    for right in range(n):
        weight += boxes[right][1]
        if right > 0 and boxes[right][0] != boxes[right - 1][0]:
            trips += 1
        while left <= right and ((right - left + 1) > maxBoxes or weight > maxWeight):
            weight -= boxes[left][1]
            if left > 0 and boxes[left][0] != boxes[left - 1][0]:
                trips -= 1
            left += 1
        dp[right + 1] = dp[left] + 2 + trips

    return dp[n]