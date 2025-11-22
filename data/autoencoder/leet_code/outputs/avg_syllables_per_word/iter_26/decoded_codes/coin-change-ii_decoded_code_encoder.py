from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        list_of_ways = [0] * (amount + 1)
        list_of_ways[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                list_of_ways[x] += list_of_ways[x - coin]

        return list_of_ways[amount]