class Solution:
    def findGameWinner(self, n: int) -> bool:
        if n % 6 != 1:
            return True
        else:
            return False