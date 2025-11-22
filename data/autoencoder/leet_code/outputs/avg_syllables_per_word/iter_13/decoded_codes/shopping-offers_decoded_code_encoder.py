from functools import lru_cache
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Filter specials: sum of offer (excluding last) > 0 and last < cost without offer
        filtered_special = [
            offer for offer in special
            if sum(offer[:-1]) > 0 and offer[-1] < sum(p * q for p, q in zip(price, offer[:-1]))
        ]

        @lru_cache(None)
        def dfs(current_needs: tuple) -> int:
            # Cost without special offers
            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in filtered_special:
                new_needs = tuple(n - o for n, o in zip(current_needs, offer[:-1]))
                if all(n >= 0 for n in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))

            return min_cost

        return dfs(tuple(needs))