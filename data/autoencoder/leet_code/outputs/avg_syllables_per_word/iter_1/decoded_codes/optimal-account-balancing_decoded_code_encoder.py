from math import inf

def min_transfers(transactions):
    balance = {}
    for sender, receiver, amount in transactions:
        balance[sender] = balance.get(sender, 0) - amount
        balance[receiver] = balance.get(receiver, 0) + amount

    balances = [amt for amt in balance.values() if amt != 0]
    if not balances:
        return 0

    def settle(start, cnt):
        while start < len(balances) and balances[start] == 0:
            start += 1
        if start == len(balances):
            return cnt

        min_cnt = inf
        for i in range(start + 1, len(balances)):
            if balances[start] * balances[i] < 0:
                balances[i] += balances[start]
                min_cnt = min(min_cnt, settle(start + 1, cnt + 1))
                balances[i] -= balances[start]
        return min_cnt

    return settle(0, 0)