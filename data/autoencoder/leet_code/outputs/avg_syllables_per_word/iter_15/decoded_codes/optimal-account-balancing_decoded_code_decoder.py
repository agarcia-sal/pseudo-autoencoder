from math import inf
from typing import List, Tuple


class Solution:
    def minTransfers(self, transactions: List[Tuple[int, int, int]]) -> int:
        balance = {}
        for from_person, to_person, amount in transactions:
            balance[from_person] = balance.get(from_person, 0) - amount
            balance[to_person] = balance.get(to_person, 0) + amount

        balances = [net_balance for net_balance in balance.values() if net_balance != 0]
        if len(balances) == 0:
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