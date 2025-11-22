from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = [
            offer for offer in special
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * o for p, o in zip(price, offer[:-1]))
        ]

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                new_needs = tuple(n - o for n, o in zip(current_needs, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    cost_with_offer = offer[-1] + dfs(new_needs)
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer
            return min_cost

        return dfs(tuple(needs))