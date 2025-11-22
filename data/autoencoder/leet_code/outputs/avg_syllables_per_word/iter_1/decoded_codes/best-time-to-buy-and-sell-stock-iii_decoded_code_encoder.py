def max_profit(prices):
    min1, min2 = float('inf'), float('inf')
    prof1, prof2 = 0, 0
    for price in prices:
        min1 = min(min1, price)
        prof1 = max(prof1, price - min1)
        min2 = min(min2, price - prof1)
        prof2 = max(prof2, price - min2)
    return prof2