from math import ceil

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2
        hours = sum(ceil(pile / mid) for pile in piles)
        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1
    return left