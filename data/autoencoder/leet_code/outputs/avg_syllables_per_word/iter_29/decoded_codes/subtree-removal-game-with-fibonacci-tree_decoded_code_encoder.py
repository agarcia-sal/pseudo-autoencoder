class Solution:
    def findGameWinner(self, n: int) -> bool:
        remainder_value = n % 6
        result = remainder_value != 1
        return result