from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        valid_special = []
        for offer in special:
            quantities = offer[:-1]
            offer_price = offer[-1]
            if sum(quantities) > 0 and offer_price < sum(p * n for p, n in zip(price, quantities)):
                valid_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in valid_special:
                new_needs = [n - o for n, o in zip(current_needs, offer[:-1])]
                if all(n >= 0 for n in new_needs):
                    cost = offer[-1] + dfs(tuple(new_needs))
                    if cost < min_cost:
                        min_cost = cost
            return min_cost

        return dfs(tuple(needs))