def max_profit(prices, fee):
    cash = 0
    hold = float('-inf')
    for p in prices:
        cash = max(cash, hold + p - fee)
        hold = max(hold, cash - p)
    return cash