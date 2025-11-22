from bisect import bisect_left

class Solution:
    def minOperations(self, target, arr):
        index_map = {v: i for i, v in enumerate(target)}
        transformed_arr = [index_map[v] for v in arr if v in index_map]
        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return len(target) - len(lis)