from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = {}
        for sender, receiver, amount in transactions:
            balance[sender] = balance.get(sender, 0) - amount
            balance[receiver] = balance.get(receiver, 0) + amount

        balances = [net for net in balance.values() if net != 0]
        if not balances:
            return 0

        def settle(start: int, count: int) -> int:
            while start < len(balances) and balances[start] == 0:
                start += 1
            if start == len(balances):
                return count

            minimum_count = float('inf')
            for i in range(start + 1, len(balances)):
                if balances[start] * balances[i] < 0:
                    balances[i] += balances[start]
                    minimum_count = min(minimum_count, settle(start + 1, count + 1))
                    balances[i] -= balances[start]
            return minimum_count

        return settle(0, 0)