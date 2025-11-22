from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            sum_of_offer_products = sum(offer[:-1])
            sum_of_price_needs_products = sum(p * n for p, n in zip(price, offer[:-1]))
            if sum_of_offer_products > 0 and offer[-1] < sum_of_price_needs_products:
                filtered_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                new_needs = [n - o for n, o in zip(current_needs, offer[:-1])]
                if all(n >= 0 for n in new_needs):
                    tentative_cost = offer[-1] + dfs(tuple(new_needs))
                    if tentative_cost < min_cost:
                        min_cost = tentative_cost
            return min_cost

        return dfs(tuple(needs))