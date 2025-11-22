from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter specials where total items > 0 and offer price < regular price
        filtered_special = []
        for offer in special:
            total_items = sum(offer[:-1])
            normal_price = sum(p * c for p, c in zip(price, offer[:-1]))
            if total_items > 0 and offer[-1] < normal_price:
                filtered_special.append(offer)

        @lru_cache(None)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, needs_tuple))
            for offer in filtered_special:
                new_needs = [n - c for n, c in zip(needs_tuple, offer[:-1])]
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))