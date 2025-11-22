from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0:
                total_price = sum(p * q for p, q in zip(price, offer[:-1]))
                if offer[-1] < total_price:
                    filtered_special.append(offer)
        special = filtered_special

        @lru_cache(None)
        def dfs(curr_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, curr_needs))
            for offer in special:
                new_needs = tuple(curr - off for curr, off in zip(curr_needs, offer[:-1]))
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))
            return min_cost

        return dfs(tuple(needs))