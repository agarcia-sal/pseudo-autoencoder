from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            offer_sum = sum(offer[:-1])
            if offer_sum > 0:
                normal_cost = sum(p * o for p, o in zip(price, offer[:-1]))
                if offer[-1] < normal_cost:
                    filtered_special.append(offer)

        def dfs(needs: Tuple[int, ...]) -> int:
            min_cost = sum(p * n for p, n in zip(price, needs))
            for offer in filtered_special:
                new_needs = []
                for n, o in zip(needs, offer[:-1]):
                    new_needs.append(n - o)
                if all(x >= 0 for x in new_needs):
                    min_cost = min(min_cost, offer[-1] + dfs(tuple(new_needs)))
            return min_cost

        return dfs(tuple(needs))