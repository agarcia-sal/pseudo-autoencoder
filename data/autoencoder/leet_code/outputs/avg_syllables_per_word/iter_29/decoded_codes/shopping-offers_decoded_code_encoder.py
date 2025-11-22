from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            sum_offer_without_last = sum(offer[:-1])
            sum_price_needs = sum(p * n for p, n in zip(price, offer[:-1]))
            if sum_offer_without_last > 0 and offer[-1] < sum_price_needs:
                filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, needs_tuple))
            for offer in special:
                new_needs = [n - o for n, o in zip(needs_tuple, offer[:-1])]
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))