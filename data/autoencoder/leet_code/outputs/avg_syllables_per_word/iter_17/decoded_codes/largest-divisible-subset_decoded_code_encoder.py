from typing import List

class Solution:
    def largestDivisibleSubset(self, list_of_numbers: List[int]) -> List[int]:
        list_of_numbers.sort()
        length_n = len(list_of_numbers)
        list_f = [1] * length_n
        index_k = 0
        for index_i in range(length_n):
            for index_j in range(index_i):
                if list_of_numbers[index_i] % list_of_numbers[index_j] == 0:
                    list_f[index_i] = max(list_f[index_i], list_f[index_j] + 1)
            if list_f[index_k] < list_f[index_i]:
                index_k = index_i
        variable_m = list_f[index_k]
        index_i = index_k
        list_ans = []
        while variable_m > 0:
            if (list_of_numbers[index_k] % list_of_numbers[index_i] == 0 
                and list_f[index_i] == variable_m):
                list_ans.append(list_of_numbers[index_i])
                index_k = index_i
                variable_m -= 1
            index_i -= 1
        return list_ans