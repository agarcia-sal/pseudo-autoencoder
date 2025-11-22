class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length_of_previous_row = 2 ** (n - 2)
        if k <= length_of_previous_row:
            return self.kthGrammar(n - 1, k)
        else:
            previous_result = self.kthGrammar(n - 1, k - length_of_previous_row)
            return 1 - previous_result