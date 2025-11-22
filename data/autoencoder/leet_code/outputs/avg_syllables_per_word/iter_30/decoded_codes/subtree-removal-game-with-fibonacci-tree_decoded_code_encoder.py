class Solution:
    def findGameWinner(self, n: int) -> bool:
        remainder = n % 6
        if remainder != 1:
            return True
        else:
            return False