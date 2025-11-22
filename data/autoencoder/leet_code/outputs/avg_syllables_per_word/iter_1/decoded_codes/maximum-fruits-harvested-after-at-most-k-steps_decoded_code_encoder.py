def maxFruits(fruits, startPos, k):
    maxF, total = 0, 0
    left = 0
    for right in range(len(fruits)):
        posR, amtR = fruits[right]
        total += amtR
        while left <= right and not (
            startPos - k <= fruits[left][0] <= startPos + k and
            startPos - k <= posR <= startPos + k and
            min(abs(posR - startPos), abs(fruits[left][0] - startPos)) + posR - fruits[left][0] <= k
        ):
            total -= fruits[left][1]
            left += 1
        maxF = max(maxF, total)
    return maxF