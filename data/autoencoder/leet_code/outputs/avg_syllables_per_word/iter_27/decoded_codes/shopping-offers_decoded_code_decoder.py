from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            total_items_in_offer = 0
            for i in range(len(offer) - 1):
                total_items_in_offer += offer[i]
            offer_cost = offer[-1]
            price_sum = 0
            for i in range(len(price)):
                price_sum += price[i] * offer[i]
            if total_items_in_offer > 0 and offer_cost < price_sum:
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(maxsize=None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = 0
            for i in range(len(price)):
                min_cost += price[i] * current_needs[i]

            for offer in special:
                new_needs = []
                for i in range(len(current_needs)):
                    remaining = current_needs[i] - offer[i]
                    new_needs.append(remaining)
                if all(n >= 0 for n in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))