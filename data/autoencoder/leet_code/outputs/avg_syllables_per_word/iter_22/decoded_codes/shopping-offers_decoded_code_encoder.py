from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            sum_of_offer_without_last = sum(offer[:-1])
            sum_of_price_multiplied_by_needs = sum(p * n for p, n in zip(price, offer[:-1]))
            if sum_of_offer_without_last > 0 and offer[-1] < sum_of_price_multiplied_by_needs:
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, needs_tuple))
            for offer in special:
                new_needs = [need - off for need, off in zip(needs_tuple, offer[:-1])]
                if all(n >= 0 for n in new_needs):
                    cost_using_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_using_offer < min_cost:
                        min_cost = cost_using_offer
            return min_cost

        return dfs(tuple(needs))