from functools import lru_cache
from typing import List, Tuple


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            # sum of items in offer except last element
            total_offer_items = sum(offer[:-1])
            # calculate cost of items in offer without the offer price
            offer_cost = sum(p * o for p, o in zip(price, offer[:-1]))
            if total_offer_items > 0 and offer[-1] < offer_cost:
                filtered_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                new_needs = []
                for n, o in zip(current_needs, offer[:-1]):
                    diff = n - o
                    if diff < 0:
                        break
                    new_needs.append(diff)
                else:  # only if never broke the loop
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))