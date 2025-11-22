from bisect import bisect_left

class Solution:
    def minOperations(self, target, arr):
        index_map = {value: i for i, value in enumerate(target)}
        transformed_arr = [index_map[val] for val in arr if val in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length