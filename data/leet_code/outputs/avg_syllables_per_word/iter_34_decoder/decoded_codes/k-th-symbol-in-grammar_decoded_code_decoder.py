class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length_of_previous_row = 2 ** (n - 1) // 2  # half the length of the current row
        if k <= length_of_previous_row:
            return self.kthGrammar(n - 1, k)
        else:
            previous_value = self.kthGrammar(n - 1, k - length_of_previous_row)
            complement_value = 1 - previous_value
            return complement_value