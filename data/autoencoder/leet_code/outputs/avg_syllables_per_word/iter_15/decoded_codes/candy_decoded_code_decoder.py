from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1
        for index in range(n - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)
        return sum(candies)