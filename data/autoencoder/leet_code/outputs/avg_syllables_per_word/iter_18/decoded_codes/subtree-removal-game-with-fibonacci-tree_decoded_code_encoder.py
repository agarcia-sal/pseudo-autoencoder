class Solution:
    def findGameWinner(self, n: int) -> bool:
        remainder_of_n_divided_by_six = n % 6
        if remainder_of_n_divided_by_six != 1:
            return True
        else:
            return False