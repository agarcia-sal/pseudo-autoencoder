from functools import lru_cache

class Solution:
    def shoppingOffers(self, price, special, needs):
        special = [
            offer for offer in special 
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * q for p, q in zip(price, offer[:-1]))
        ]

        @lru_cache(None)
        def dfs(needs):
            min_cost = sum(p * n for p, n in zip(price, needs))
            for offer in special:
                new_needs = tuple(n - q for n, q in zip(needs, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))
            return min_cost

        return dfs(tuple(needs))