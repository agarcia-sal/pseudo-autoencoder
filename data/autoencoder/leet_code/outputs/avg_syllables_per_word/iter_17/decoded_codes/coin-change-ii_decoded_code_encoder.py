class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        list_of_ways = [0] * (amount + 1)
        list_of_ways[0] = 1
        for coin in coins:
            for index in range(coin, amount + 1):
                list_of_ways[index] += list_of_ways[index - coin]
        return list_of_ways[amount]