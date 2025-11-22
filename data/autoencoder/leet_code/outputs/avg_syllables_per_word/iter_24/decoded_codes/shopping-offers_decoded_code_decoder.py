from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        filtered_special = []
        for offer in special:
            if sum(offer[:-1]) > 0:
                total_price = sum(p * n for p, n in zip(price, offer[:-1]))
                if offer[-1] < total_price:
                    filtered_special.append(offer)

        memo = {}

        def dfs(current_needs: Tuple[int, ...]) -> int:
            if current_needs in memo:
                return memo[current_needs]

            min_cost = sum(p * n for p, n in zip(price, current_needs))

            for offer in filtered_special:
                new_needs = [n - o for n, o in zip(current_needs, offer[:-1])]

                if all(n >= 0 for n in new_needs):
                    cost_with_offer = offer[-1] + dfs(tuple(new_needs))
                    if cost_with_offer < min_cost:
                        min_cost = cost_with_offer

            memo[current_needs] = min_cost
            return min_cost

        return dfs(tuple(needs))