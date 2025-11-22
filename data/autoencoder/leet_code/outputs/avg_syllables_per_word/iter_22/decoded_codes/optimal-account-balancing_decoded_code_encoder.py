from math import inf
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = {}
        for frm, to, amount in transactions:
            if frm not in balance:
                balance[frm] = 0
            if to not in balance:
                balance[to] = 0
            balance[frm] -= amount
            balance[to] += amount

        balances = [net for net in balance.values() if net != 0]
        if not balances:
            return 0

        def settle(start: int, cnt: int) -> int:
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