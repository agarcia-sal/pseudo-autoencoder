from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            offer_counts = offer[:-1]
            offer_price = offer[-1]
            if sum(offer_counts) > 0:
                total_price = sum(p * c for p, c in zip(price, offer_counts))
                if offer_price < total_price:
                    filtered_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                offer_counts = offer[:-1]
                offer_price = offer[-1]
                new_needs = tuple(n - o for n, o in zip(current_needs, offer_counts))
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer_price + dfs(new_needs)
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))