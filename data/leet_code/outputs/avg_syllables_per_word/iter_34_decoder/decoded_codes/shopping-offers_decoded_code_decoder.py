from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            total_items_in_offer = 0
            for i in range(len(offer) - 1):
                total_items_in_offer += offer[i]
            total_price_of_offer = 0
            for i in range(len(offer) - 1):
                total_price_of_offer += offer[i] * price[i]
            if total_items_in_offer > 0 and offer[-1] < total_price_of_offer:
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            min_cost = 0
            for i in range(len(needs_tuple)):
                min_cost += price[i] * needs_tuple[i]

            for offer in special:
                new_needs = []
                for i in range(len(offer) - 1):
                    updated_need = needs_tuple[i] - offer[i]
                    new_needs.append(updated_need)
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))