import bisect

class Solution:
    def minOperations(self, target, arr):
        index_map = {value: idx for idx, value in enumerate(target)}
        transformed_arr = [index_map[value] for value in arr if value in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        minimum_operations = len(target) - lcs_length
        return minimum_operations