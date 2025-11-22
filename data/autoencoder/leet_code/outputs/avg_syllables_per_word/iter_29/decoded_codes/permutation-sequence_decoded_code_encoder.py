from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        list_of_numbers = list(range(1, n + 1))
        adjusted_k = k - 1
        result_list = []
        for i in range(n, 0, -1):
            factorial_value = factorial(i - 1)
            index_value = adjusted_k // factorial_value
            result_list.append(str(list_of_numbers.pop(index_value)))
            adjusted_k %= factorial_value
        final_result = ''.join(result_list)
        return final_result