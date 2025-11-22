class Solution:
    def minTransfers(self, transactions):
        balance = {}
        for frm, to, amount in transactions:
            balance[frm] = balance.get(frm, 0) - amount
            balance[to] = balance.get(to, 0) + amount

        balances = [v for v in balance.values() if v != 0]
        if not balances:
            return 0

        def settle(start, cnt):
            while start < len(balances) and balances[start] == 0:
                start += 1
            if start == len(balances):
                return cnt
            min_cnt = float('inf')
            for i in range(start + 1, len(balances)):
                if balances[start] * balances[i] < 0:
                    balances[i] += balances[start]
                    min_cnt = min(min_cnt, settle(start + 1, cnt + 1))
                    balances[i] -= balances[start]
            return min_cnt

        return settle(0, 0)