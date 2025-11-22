class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length_of_previous_row = (1 << (n - 1)) - 1
        if k <= length_of_previous_row:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - length_of_previous_row)