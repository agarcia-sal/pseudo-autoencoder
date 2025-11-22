from functools import lru_cache
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter out offers that do not reduce cost or don't provide any items
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0:
                offer_price = offer[-1]
                regular_price = sum(p * o for p, o in zip(price, offer[:-1]))
                if offer_price < regular_price:
                    filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(needs_tup):
            min_cost = sum(p * n for p, n in zip(price, needs_tup))
            for offer in special:
                new_needs = tuple(n - o for n, o in zip(needs_tup, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(new_needs)
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))