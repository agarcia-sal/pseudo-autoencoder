from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = {}
        for transaction in transactions:
            frm = transaction[0]
            to = transaction[1]
            amount = transaction[2]

            if frm not in balance:
                balance[frm] = 0
            balance[frm] -= amount

            if to not in balance:
                balance[to] = 0
            balance[to] += amount

        balances = [v for v in balance.values() if v != 0]

        if len(balances) == 0:
            return 0

        def settle(start: int, cnt: int) -> int:
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