from functools import lru_cache
from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * n for p, n in zip(price, offer[:-1])):
                filtered_special.append(offer)

        @lru_cache(None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, current_needs))
            for offer in filtered_special:
                new_needs = [n - o for n, o in zip(current_needs, offer[:-1])]
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(tuple(new_needs)))
            return min_cost

        return dfs(tuple(needs))